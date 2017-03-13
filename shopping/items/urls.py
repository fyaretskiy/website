from .views import ItemsView, AddItemView, DeleteItemView

from django.conf.urls import url


urlpatterns = [
    url(r'^$', ItemsView.as_view(), name='home'),
    url(r'^add-item/(?P<item_id>[0-9]+)$', AddItemView.as_view(),
        name='add_item'),
    url(r'^remove-item/(?P<item_id>[0-9]+)$', DeleteItemView.as_view(),
        name='remove_item')
]