from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering = ('-id',)