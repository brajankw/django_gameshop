from django.urls import path

from .views import (
    ProductDetailView,
    cart,
    product_list,
    CategoryListView,
)


urlpatterns = [
    path("", product_list, name="product_list"),
    path("products/all/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("products/<category>", CategoryListView.as_view(), name="category_list"),
    path("cart", cart, name="cart"),
]
