from django.contrib import admin

from .models import Category, Question


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "owner",
    )
    list_select_related = ("owner",)
    search_fields = ("user__username",)
    list_filter = (
        "owner",
        "name",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "choice",
        "question",
    )
    list_select_related = ("choice",)
    search_fields = (
        "choice__name",
        "choice__id",
    )
    list_filter = (
        "choice",
        "question",
    )
