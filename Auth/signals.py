from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from Auth.models import LoggedInUser, User, Profile

from channels_presence.signals import presence_changed
from channels import Group

@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))

@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
