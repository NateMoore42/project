import time
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.cache import cache
from django.contrib.sites.models import Site

import settings

class LastSeenManager(models.Manager):
    def seen(self, user, module=settings.LAST_SEEN_DEFAULT_MODULE, force=False, site=None):
        if not site:
            site = Site.objects.get_current()
        args = {
            'user': user,
            'site': site,
            'module': module,
        }
        seen, created = self.get_or_create(**args)
        if created:
            return seen

        limit = timezone.now() - datetime.timedelta(seconds=settings.LAST_SEEN_INTERVAL)
        if seen.last_seen < limit or force:
            seen.last_seen = timezone.now()
            seen.save()

        return seen

    def when(self, user, module=None, site=None):
        args = {'user': user}
        if module:
            args['module'] = module
        if site:
            args['site'] = site
        return self.filter(**args).latest('last_seen').last_seen

class LastSeen(models.Model):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    module = models.CharField(default=settings.LAST_SEEN_DEFAULT_MODULE, max_length=20)
    last_seen = models.DateTimeField(default=timezone.now)

    objects = LastSeenManager()

    class Meta:
        verbose_name = ('Last Seen')
        verbose_name_plural = ('Last Seen')
        unique_together = (('user', 'site', 'module'),)
        ordering = ('-last_seen',)

    def __unicode__(self):
        return u"%s on %s" % (self.user, self.last_seen)

def get_cache_key(site, module, user):
    return "last_seen:%s:%s:%s" % (site.id, module, user.pk)

def user_seen(user, module=settings.LAST_SEEN_DEFAULT_MODULE, site=None):
    if not site:
        site = Site.objects.get_current()
    cache_key = get_cache_key(site, module, user)
    limit = time.time() - settings.LAST_SEEN_INTERVAL
    seen = cache.get(cache_key)
    if not seen or seen < limit:
        if seen == -1:
            LastSeen.objects.seen(user, module=module, site=site, force=True)
        else:
            LastSeen.objects.seen(user, module=module, site=site)
        timeout = settings.LAST_SEEN_INTERVAL
        cache.set(cache_key, time.time(), timeout)

def clear_interval(user):
    keys = {}
    for last_seen in LastSeen.objects.filter(user=user):
        cache_key = get_cache_key(last_seen.site, last_seen.module, user)
        keys[cache_key] = -1

    if keys:
        cache.set_many(keys)
