from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', default='static/default_img/123.jpg')
    age = models.PositiveSmallIntegerField(blank=True, null=True)
