from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post
from django.utils import timezone
from blogicum.settings import POSTS_RELEASE_LIMIT

# Create your views here.


def get_select_related(limit=None, category_slug=None):
    select_related_variable = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    if limit is None:
        return select_related_variable.filter(category__slug=category_slug)
    return select_related_variable[:limit]


def index(request):
    context = {'posts': get_select_related(limit=POSTS_RELEASE_LIMIT)}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    posts = get_select_related(category_slug=category_slug)
    if not posts.exists():
        raise Http404("Категория не найдена")
    selected_context = {
        'category': category_slug,
        'posts': posts
    }
    return render(request, 'blog/category.html', selected_context)
