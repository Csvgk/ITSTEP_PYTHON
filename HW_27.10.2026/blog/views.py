from django.shortcuts import render
from django.utils import timezone

from .models import Post, Category, Tag


def dummy():
    return "func working!"


# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {'posts': posts, 'categories': categories, 'tags': tags}
    return render(request, 'blog/index.html', context)


def get_post(request):
    context = {}
    return render(request, 'blog/post.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)
