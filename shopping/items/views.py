from django.views.generic.list import ListView, View
from django.shortcuts import reverse
from items.models import Item
from django.http import HttpResponseRedirect


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
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))


class DeleteItemView(ListView):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            item = Item.objects.get(id=self.kwargs['item_id'])
            user.delete_item_from_list(item)

        return super().dispatch(request, *args, **kwargs)