from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import CommentForm, SubscribeForm
from .models import Category, Post, Tag


def sidebar_context():
    categories = list(Category.objects.all())
    half = (len(categories) + 1) // 2
    return {
        'categories': categories[:half],
        'categories2': categories[half:],
        'tags': Tag.objects.all(),
        'subscribe_form': SubscribeForm(),
    }


def index(request):
    posts = Post.objects.select_related('category', 'user').prefetch_related('tags')
    context = {'posts': posts, **sidebar_context()}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'user').prefetch_related('tags'), id=post_id
    )

    form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('admin:login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Коментар опубліковано.')
            return redirect('blog:post_detail', post_id=post.id)

    comments = post.comments.select_related('author')
    context = {'post': post, 'comments': comments, 'form': form, **sidebar_context()}
    return render(request, 'blog/post_detail.html', context)


def profile_detail(request, user_id):
    author = get_object_or_404(User, id=user_id)
    posts = author.post_set.select_related('category')
    profile = getattr(author, 'profile', None)
    context = {'author': author, 'profile': profile, 'posts': posts, **sidebar_context()}
    return render(request, 'blog/profile_detail.html', context)


def contact(request):
    return render(request, 'blog/contact.html', sidebar_context())


@require_POST
def subscribe(request):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Ви успішно підписалися!')
    else:
        for error in form.errors.get('email', []):
            messages.error(request, error)

    next_url = request.POST.get('next', '')
    if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        return redirect(next_url)
    return redirect('blog:index')
