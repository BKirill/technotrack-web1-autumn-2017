from django.db import models
from django.conf import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    post = models.ForeignKey('posts.Post', related_name='comments')
    parent = models.ForeignKey('self', blank=True, null=True)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Комментарий к посту ' + self.post.title

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ('-created_at',)