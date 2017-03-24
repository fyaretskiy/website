from django.db import models
from django.shortcuts import reverse


class Item(models.Model):
    name = models.CharField('name', max_length=128)

    def add_to_shopping_list_url(self):
        return reverse('items:add_item', kwargs={'item_id': self.pk})

    def __str__(self):
        return self.name


class UserPurchasedItem(models.Model):
    RELATED_NAME = 'user_purchased_items'

    user = models.ForeignKey('user.User', related_name=RELATED_NAME)
    list_item = models.ForeignKey(Item, related_name=RELATED_NAME)

    def __str__(self):
        return '{}:{}'.format(self.user, self.list_item)


class UserShoppingListItem(models.Model):
    RELATED_NAME = 'user_shopping_list_items'

    user = models.ForeignKey('user.User', related_name=RELATED_NAME)
    list_item = models.ForeignKey(Item, related_name=RELATED_NAME)

    def __str__(self):
        return '{}:{}'.format(self.user, self.list_item)
