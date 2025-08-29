from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post
# from django.core.paginator import Paginator

# Create your views here.


def index(request):
    posts = Post.objects.all()
    # # С добавлением пагинации
    # paginator = Paginator(posts, 10)  # Добавил пагинацию
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # context = {'posts': page_obj}

    # Без пагинации
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    posts = Post.objects.filter(category=category_slug)
    if not posts.exists():
        raise Http404("Категория не найдена")
    selected_context = {
        'selected_category': category_slug,
        'posts': posts
    }
    return render(request, 'blog/category.html', selected_context)






















# ----------
# # blogicum/blog/views.py
# 
# # Полная копия старого рабочего кода
# 
# 
# from django.shortcuts import render
# from django.http import Http404
# from typing import List, Dict
# 
# 
# # Create your views here.
# 
# 
# posts: List[Dict[str, object]] = [
#     {
#         'id': 0,
#         'location': 'Остров отчаянья',
#         'date': '30 сентября 1659 года',
#         'category': 'travel',
#         'text': '''Наш корабль, застигнутый в открытом море
#                 страшным штормом, потерпел крушение.
#                 Весь экипаж, кроме меня, утонул; я же,
#                 несчастный Робинзон Крузо, был выброшен
#                 полумёртвым на берег этого проклятого острова,
#                 который назвал островом Отчаяния.''',
#     },
#     {
#         'id': 1,
#         'location': 'Остров отчаянья',
#         'date': '1 октября 1659 года',
#         'category': 'not-my-day',
#         'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
#                 с мели приливом и пригнало гораздо ближе к берегу.
#                 Это подало мне надежду, что, когда ветер стихнет,
#                 мне удастся добраться до корабля и запастись едой и
#                 другими необходимыми вещами. Я немного приободрился,
#                 хотя печаль о погибших товарищах не покидала меня.
#                 Мне всё думалось, что, останься мы на корабле, мы
#                 непременно спаслись бы. Теперь из его обломков мы могли бы
#                 построить баркас, на котором и выбрались бы из этого
#                 гиблого места.''',
#     },
#     {
#         'id': 2,
#         'location': 'Остров отчаянья',
#         'date': '25 октября 1659 года',
#         'category': 'not-my-day',
#         'text': '''Всю ночь и весь день шёл дождь и дул сильный
#                 порывистый ветер. 25 октября.  Корабль за ночь разбило
#                 в щепки; на том месте, где он стоял, торчат какие-то
#                 жалкие обломки,  да и те видны только во время отлива.
#                 Весь этот день я хлопотал  около вещей: укрывал и
#                 укутывал их, чтобы не испортились от дождя.''',
#     },
# ]
# 
# 
# POSTS_DICT = {post['id']: post for post in posts}
# 
# 
# def index(request, posts=posts):
#     context = {'posts': posts[::-1]}
#     return render(request, 'blog/index.html', context)
# 
# 
# def post_detail(request, post_id):
#     if post_id not in POSTS_DICT:
#         raise Http404
#     context = {'post': POSTS_DICT[post_id]}
#     return render(request, 'blog/detail.html', context)
# 
# 
# def category_posts(request, category_slug):
#     posts_by_category_slug = [
#         post for post in posts if post['category'] == category_slug
#     ]
#     selected_context = {
#         'selected_category': category_slug,
#         'post': posts_by_category_slug
#     }
#     return render(request, 'blog/category.html', selected_context)
# 

