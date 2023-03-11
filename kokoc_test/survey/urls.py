from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ice_cream/', views.ice_cream_list),
]
