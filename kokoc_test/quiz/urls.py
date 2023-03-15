from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("category/", views.index_page, name="index_page"),
    path("category/auth/", views.index_page, name="index_page"),
    path("best_users/", views.best_users, name="best_users"),
    path("category/<int:pk>/", views.take_quiz, name="take_quiz"),
]
