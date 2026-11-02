from django.shortcuts import render


# page — назва сторінки, за нею в base.html підсвічується активний пункт меню
def index(request):
    return render(request, 'keepsimple/index.html', {'page': 'index'})


def blog(request):
    return render(request, 'keepsimple/blog.html', {'page': 'blog'})


def single(request):
    return render(request, 'keepsimple/single.html', {'page': 'single'})


def page(request):
    return render(request, 'keepsimple/page.html', {'page': 'page'})


def archives(request):
    return render(request, 'keepsimple/archives.html', {'page': 'archives'})


def demo(request):
    return render(request, 'keepsimple/demo.html', {'page': 'demo'})
