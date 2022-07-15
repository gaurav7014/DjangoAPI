from django.contrib import admin

from products.models import Category, Product, ProductImages, QuantityVariant

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ProductImages)