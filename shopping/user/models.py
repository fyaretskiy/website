from django.contrib.auth.models import User as UserModel
from django.db import models

from items.models import Item, UserPurchasedItem, UserShoppingListItem


class User(UserModel):

    shopping_list_items = models.ManyToManyField(
        Item, through=UserShoppingListItem,
        related_name='shopping_list_item_users')

    purchased_items = models.ManyToManyField(
        Item, through=UserPurchasedItem,
        related_name='purchased_item_users')

    def get_shopping_list_items(self):
        return self.shopping_list_items.all()

    def get_purchased_items(self):
        return self.purchased_items.all()

    def add_item_to_shopping_list(self, item):
        UserShoppingListItem.objects.create(user=self, item=item)

    def delete_item_from_list(self, item):
        UserShoppingListItem.objects.filter(user=self, item=item).delete()

    def __str__(self):
        return self.username
