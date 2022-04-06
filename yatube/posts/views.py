from django.shortcuts import render, get_object_or_404
from .models import Post, Group
# from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_post(request, slug):
    template = 'posts/group_list.html'
    title = 'Записи сообщества '
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
        'group': group
    }
    return render(request, template, context)
