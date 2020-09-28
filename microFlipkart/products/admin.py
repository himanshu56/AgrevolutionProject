from django.contrib import admin

# Register your models here.
from .models import Product, ProductVariant

#admin.site.register(Product)
#admin.site.register(ProductVariant)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register the Admin classes for BookInstance using the decorator
@admin.register(ProductVariant) 
class ProductVarientAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'size', 'texture', 'price')