from django.contrib import admin
from .models import Post
from .models import Category
from .models import Location
from django.contrib.auth.models import Group

# Register your models here.


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'pub_date',
        'is_published',
        'created_at',
        'author',
        'category__title',
        'location__name',
    )
    list_editable = (
        'is_published',
        'author',
    )
    search_fields = ('title', 'text')
    list_filter = ('category__title',)
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('created_at',)
    list_display_links = ('name',)
