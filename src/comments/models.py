from django.db import models


class AbstractComment(models.Model):
    '''Абстрактная модель комментария'''
    text = models.TextField(max_length=512, null=True, blank=True)
    create_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    # moderation = models.BooleanField(default=False)
    # like_count = models.PositiveBigIntegerField(default=0)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_comments')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract = True
