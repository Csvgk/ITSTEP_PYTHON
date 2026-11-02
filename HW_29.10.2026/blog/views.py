from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Comment, Post, Tag


def sidebar_context():
    """Категорії (у дві колонки) і теги для бічної панелі на всіх сторінках."""
    categories = list(Category.objects.all())
    half = (len(categories) + 1) // 2
    return {
        'categories': categories[:half],
        'categories2': categories[half:],
        'tags': Tag.objects.all(),
    }


# #1 Головна сторінка: пости з бази через ORM
def index(request):
    posts = Post.objects.select_related('category', 'user').prefetch_related('tags')
    context = {'posts': posts, **sidebar_context()}
    return render(request, 'blog/index.html', context)


# #2 Сторінка окремого поста
def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'user').prefetch_related('tags'), id=post_id
    )

    # #3 Додавання коментаря (тільки для користувачів, які увійшли)
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(post=post, author=request.user, text=text)
        return redirect('blog:post_detail', post_id=post.id)

    comments = post.comments.select_related('author')
    context = {'post': post, 'comments': comments, **sidebar_context()}
    return render(request, 'blog/post_detail.html', context)


# #3 Сторінка профілю автора
def profile_detail(request, user_id):
    author = get_object_or_404(User, id=user_id)
    posts = author.post_set.select_related('category')
    profile = getattr(author, 'profile', None)
    context = {'author': author, 'profile': profile, 'posts': posts, **sidebar_context()}
    return render(request, 'blog/profile_detail.html', context)


def contact(request):
    return render(request, 'blog/contact.html', sidebar_context())
