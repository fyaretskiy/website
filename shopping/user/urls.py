from django.conf.urls import url

from .views import LoginView, LogoutView, UserRegistrationView

urlpatterns = [
    url(r'^registration', UserRegistrationView.as_view(), name='registration'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^login$', LoginView.as_view(), name='login'),
]
