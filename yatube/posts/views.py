# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_post(request, slug):
    return HttpResponse(f'Посты групп {slug}')
