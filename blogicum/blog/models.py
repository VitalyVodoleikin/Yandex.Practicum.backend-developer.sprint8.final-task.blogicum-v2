from django.db import models
from django.contrib.auth import get_user_model


# Пользователь, эту модель описывать не нужно, она встроена в Django
User = get_user_model()


class Post(models.Model):
    # Публикация
    title = models.CharField(
        max_length=256, 
        blank=False, 
        null=False, 
        verbose_name='Заголовок'
    )
    text = models.TextField(
        blank=False, 
        null=False, 
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, 
        blank=False, 
        null=False, 
        verbose_name='Дата и время публикации', 
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        blank=False, 
        null=False, 
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        'Location', 
        on_delete=models.SET_NULL, 
        blank=False, 
        null=True, 
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL, 
        blank=False, 
        null=True, 
        verbose_name='Категория'
    )
    is_published = models.BooleanField(
        default=True, 
        blank=False, 
        null=False, 
        verbose_name='Опубликовано', 
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        blank=False, 
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

        def __str__(self):
            return self.title


class Category(models.Model):
    # Тематическая категория
    title = models.CharField(
        max_length=256, 
        blank=False, 
        null=False, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        blank=False, 
        null=False, 
        verbose_name='Описание'
    )
    slug = models.SlugField(
        blank=False, 
        unique=True, 
        null=False, 
        verbose_name='Идентификатор', 
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    is_published = models.BooleanField(
        default=True, 
        blank=False, 
        null=False, 
        verbose_name='Опубликовано', 
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        blank=False, 
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

        def __str__(self):
            return self.title


class Location(models.Model):
    # Географическая метка
    name = models.CharField(
        max_length=256, 
        blank=False, 
        null=False, verbose_name='Название места'
    )
    is_published = models.BooleanField(
        default=True, 
        blank=False, 
        null=False, verbose_name='Опубликовано', 
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        blank=False, 
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

        def __str__(self):
            return self.title
























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
