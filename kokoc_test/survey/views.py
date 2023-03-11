from django.shortcuts import render
from django.http import HttpResponse


def index(request):    
    return HttpResponse('Главная страница')


def ice_cream_list(request):
    return HttpResponse('Список тестов')
