from django.conf.urls import url, include
from .views import UserRegistrationView

urlpatterns = [
    url(r'^registration', UserRegistrationView.as_view(), name='registration'),
]
