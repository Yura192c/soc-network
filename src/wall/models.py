from django.db import models
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from src.comments.models import AbstractComment


class Post(models.Model):
    '''Пост на стене юзера'''

    text = models.TextField(max_length=1000, null=True, blank=True)
    create_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=False)
    view_count = models.PositiveBigIntegerField('Просмотры', default=0)
    # like_count = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'Post by {self.user}'

    def comments_count(self):
        return self.comments.filter(published=True).count()

class Comment(AbstractComment, MPTTModel):
    """ Модель коментариев к постам"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
