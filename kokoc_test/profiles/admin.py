from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "scores",)
    search_fields = ("username", "email", "first_name",)
    list_filter = ("background_color", "first_name", "last_name",)
