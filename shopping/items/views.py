from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.list import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item


class ItemsView(ListView):

    paginate_by = 20
    model = Item
    template_name = 'items/items.html'

    def get_queryset(self):
        return self.model.objects.all()


class AddItemView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['item_id'])
        request.user.add_item_to_shopping_list(item)
        return HttpResponseRedirect(reverse('items:shopping_list'))


class DeleteItemView(LoginRequiredMixin, ListView):
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['item_id'])
        request.user.delete_item_from_list(item)

        return HttpResponseRedirect(reverse('items:shopping_list'))


class ShoppingListView(ListView):
    paginate_by = 20
    model = Item
    template_name = 'items/shopping_list.html'

    def get_queryset(self):
        return self.request.user.get_shopping_list_items()
