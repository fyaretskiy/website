from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.list import ListView, View

from items.models import Item


class ItemsView(ListView):

    paginate_by = 20
    model = Item
    template_name = 'items/items.html'

    def get_queryset(self):
        return self.model.objects.all()


class AddItemView(View):

    def dispatch(self, request, *args, **kwargs):

        user = request.user
        if user.is_authenticated:
            item = Item.objects.get(id=self.kwargs['item_id'])
            user.add_item_to_shopping_list(item)
            return HttpResponseRedirect(reverse('items:home'))
        else:
            return HttpResponseRedirect(reverse('items:home'))


class DeleteItemView(ListView):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            item = Item.objects.get(id=self.kwargs['item_id'])
            user.delete_item_from_list(item)

        return super().dispatch(request, *args, **kwargs)


class ShoppingListView(ListView):
    paginate_by = 20
    model = Item
    template_name = 'items/shopping_list.html'

    def get_queryset(self):
        return self.request.user.get_shopping_list_items()
