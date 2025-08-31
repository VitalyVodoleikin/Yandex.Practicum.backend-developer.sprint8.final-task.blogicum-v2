from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post
from datetime import datetime


# Create your views here.


def index(request):
    posts = Post.objects.select_related(
        'category'
    ).filter(
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by(
        '-pub_date'
    )[:5]

    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    posts = Post.objects.select_related(
        'category'
    ).filter(
        category__slug=category_slug,
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by(
        '-pub_date'
    )
    if not posts.exists():
        raise Http404("Категория не найдена")
    selected_context = {
        'category': category_slug,
        'posts': posts
    }
    return render(request, 'blog/category.html', selected_context)
