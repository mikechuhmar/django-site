from django.contrib import admin
from ecomapp.models import Category, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Модель товара
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Brand)
'''admin.site.register(Category)

admin.site.register(Product)'''
