from django.db import models
from django.contrib.auth import get_user_model


# Пользователь, эту модель описывать не нужно, она встроена в Django
User = get_user_model()


class Category(models.Model):
    # Тематическая категория
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    slug = models.SlugField(blank=False, unique=True, null=False)
    is_published = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)


class Location(models.Model):
    # Географическая метка
    name = models.CharField(max_length=256, blank=False, null=False)
    is_published = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)


class Post(models.Model):
    # Публикация
    title = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
    is_published = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)






# ----------
# Позже удалить это
# Пример кода из задания с Анфисой
# class IceCream(PublishedModel):
#     title = models.CharField(max_length=256, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     wrapper = models.OneToOneField(
#         Wrapper,
#         on_delete=models.SET_NULL,
#         related_name='ice_cream',
#         null=True,
#         blank=True,
#         verbose_name='Обертка'
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name='ice_creams',
#         verbose_name='Категория',
#     )
#     toppings = models.ManyToManyField(Topping)
#     is_on_main = models.BooleanField(default=False, verbose_name='На главную')
#     output_order = models.PositiveSmallIntegerField(
#         default=100,
#         verbose_name='Порядок отображения'
#     )
#     price = models.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         verbose_name = 'Мороженое'
#         verbose_name_plural = 'Мороженое'
#         # Сначала сортируем по полю output_order, 
#         # а если у нескольких объектов значения output_order совпадают-- 
#         # сортируем по title.
#         ordering = ('output_order', 'title')

#     def __str__(self):
#         return self.title
