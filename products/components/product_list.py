from django.contrib.auth import get_user_model
from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from products.models import UserItem

CustomUser = get_user_model()


class ProductListView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user_pk: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.user_pk = kwargs.get("user")
        self.user_products = UserItem.objects.filter(user=self.user_pk)

    def add_item(self, product_pk):
        item, created = UserItem.objects.get_or_create(
            user_id=self.user_pk, product_id=product_pk
        )
        if not created:
            item.quantity = F("quantity") + 1
            item.save()
        self.user_products = UserItem.objects.filter(user=self.user_pk)
