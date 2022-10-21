from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"


@login_required
def cart(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/cart.html", context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/product_list.html", context)


class CategoryListView(ListView):

    template_name = "products/category_list.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs["category"])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        print(context)
        return context
