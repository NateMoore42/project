from __future__ import unicode_literals

from django.db import models

from Auth.models import User

class Game(models.Model):
    creator = models.ForeignKey(User, related_name='creator')
    player = models.ForeignKey(User, related_name='player')
