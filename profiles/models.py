from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNet(AbstractUser):
    '''Custom user model'''
    GENDER = {
        ('M', 'Мужской'),
        ('W', 'Женский'),
        ('N', 'Нет'),
    }
    gender = models.CharField(max_length=1, choices=GENDER, default='N')
    image = models.ImageField(upload_to='user/image/', blank=True, null=True)
    first_login = models.DateTimeField(null=True)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

