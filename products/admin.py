from itertools import product
from django.contrib import admin

from .models import Product, UserItem, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description", "price")


class UserItemAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "quantity", "added")


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserItem, UserItemAdmin)
