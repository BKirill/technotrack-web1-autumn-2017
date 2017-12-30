from django.db import models
from django.conf import settings

class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = ('-created_at',)