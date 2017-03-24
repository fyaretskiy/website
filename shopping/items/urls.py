from django.conf.urls import url

from .views import AddItemView, DeleteItemView, ItemsView, ShoppingListView

urlpatterns = [
    url(r'^$', ItemsView.as_view(), name='home'),
    url(r'^shopping-list$', ShoppingListView.as_view(),
        name='shopping_list'),
    url(r'^add-item/(?P<item_id>[0-9]+)$', AddItemView.as_view(),
        name='add_item'),
    url(r'^remove-item/(?P<item_id>[0-9]+)$', DeleteItemView.as_view(),
        name='remove_item')
]
