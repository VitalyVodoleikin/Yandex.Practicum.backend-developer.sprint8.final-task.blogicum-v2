from django.db import models
from django.contrib.auth import get_user_model
from blogicum.settings import MAX_LENGTH_TITLE_FIELDS, MAX_LENGTH_SELF_TITLE

# Пользователь, эту модель описывать не нужно, она встроена в Django
User = get_user_model()


class PublishAbstractModel(models.Model):
    # Абстрактная модель с общими полями публикации
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Post(PublishAbstractModel):
    # Публикация
    title = models.CharField(
        max_length=MAX_LENGTH_TITLE_FIELDS,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now=False,
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в '
            'будущем — можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
        related_name='posts'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'
        ordering = ('-pub_date',)

        def __str__(self):
            if len(self.title) > MAX_LENGTH_SELF_TITLE:
                return f"{self.title[:MAX_LENGTH_SELF_TITLE]}"
            return f"{self.title}"


class Category(PublishAbstractModel):
    # Тематическая категория
    title = models.CharField(
        max_length=MAX_LENGTH_TITLE_FIELDS,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'

        def __str__(self):
            if len(self.title) > MAX_LENGTH_SELF_TITLE:
                return f"{self.title[:MAX_LENGTH_SELF_TITLE]}"
            return f"{self.title}"


class Location(PublishAbstractModel):
    # Географическая метка
    name = models.CharField(
        max_length=MAX_LENGTH_TITLE_FIELDS,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
        default_related_name = 'locations'

        def __str__(self):
            if len(self.title) > MAX_LENGTH_SELF_TITLE:
                return f"{self.title[:MAX_LENGTH_SELF_TITLE]}"
            return f"{self.title}"
