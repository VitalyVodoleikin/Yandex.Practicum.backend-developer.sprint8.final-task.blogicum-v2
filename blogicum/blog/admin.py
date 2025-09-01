from django.contrib import admin
from .models import Post
from .models import Category
from .models import Location

# Register your models here.


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


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
