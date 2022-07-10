from django.contrib import admin
from .models import Product, Category, Comment

class ProductAdmin(admin.ModelAdmin):
    """
    For products in the admin area.
    """
    list_display = (
        'pk',
        'name',
        'category',
        'description',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    """
    For categories in the admin area.
    """
    list_display = (
        'name',
        'friendly_name',
    )

class CommentAdmin(admin.ModelAdmin):
    """
    For comments in the admin area.
    """
    list_display = ('author', 'title', 'product', 'date_created')
    list_filter = ('product', 'date_created')
    search_fields = ['author', 'title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)