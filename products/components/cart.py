from django.contrib.auth import get_user_model
from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from products.models import UserItem

CustomUser = get_user_model()


class CartView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user_pk: int
    total: float = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.user_pk = kwargs.get("user")
        self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.get_total()

    def delete_item(self, product_pk):
        item = UserItem.objects.filter(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

    def get_total(self):
        self.total = sum(product.total_price for product in self.user_products)
