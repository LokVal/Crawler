from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from crawler.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
