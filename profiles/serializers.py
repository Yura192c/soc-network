from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    '''info about user'''

    class Meta:
        model = UserNet
        exclude = ('password',
                   'groups',
                   'user_permissions',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser')


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    '''Публичная информация'''

    class Meta:
        model = UserNet
        exclude = ('password',
                   'email',
                   'groups',
                   'user_permissions',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser')
