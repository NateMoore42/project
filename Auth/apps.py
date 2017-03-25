from __future__ import unicode_literals

from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'Auth'
    verbose_name = 'Accounts'
    icon = '<i class="material-icons">people</i>'

    def ready(self):
        import Auth.signals
