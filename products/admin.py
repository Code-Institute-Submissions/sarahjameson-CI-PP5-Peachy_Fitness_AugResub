from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'name',
        'friendly_name',
    )   

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)