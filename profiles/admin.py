from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet


# admin.site.register(UserNet, UserAdmin)

@admin.register(UserNet)
class UserNetAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
