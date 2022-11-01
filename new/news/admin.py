from django.contrib import admin

# Register your models here.
from .models import News, Category, SuperCategory


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'cost', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    filter_horizontal = ['categores']


class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    filter_horizontal = ['categores']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(Category, CategoryAdmin)