from django.db import models
from django.conf import settings


class PostQuerySet(models.QuerySet):

    def available_for_user(self, user):

        return self.filter(models.Q(is_deleted=False) | models.Q(author_id=user.id))


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    blog = models.ForeignKey('blogs.Blog', related_name='posts')
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    categories = models.ManyToManyField('categories.Category', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    likes_count = models.IntegerField(default=0)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title + ' в блоге ' + self.blog.title

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-created_at',)


class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey('posts.Post', related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'