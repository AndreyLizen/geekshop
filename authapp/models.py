from datetime import timedelta
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', default='static/default_img/123.jpg')
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=18)

    activation_key = models.CharField(max_length=64, blank=True, null=True)
    activation_key_expires = models.DateTimeField(default=now() + timedelta(hours=48))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
