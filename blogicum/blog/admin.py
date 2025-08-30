from django.contrib import admin
from .models import Post
from .models import Category
from .models import Location

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'is_published',
        'created_at',
        'author',
        'category',
        'location',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
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
        'name',
        'is_published',
        'created_at',
    )
    # list_editable = (
    #     'name',
    # )
    search_fields = ('name',) 
    list_filter = ('name',)
    list_display_links = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
