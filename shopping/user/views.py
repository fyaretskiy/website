from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.edit import FormView, View

from .forms import UserLoginForm, UserRegistrationForm


class UserRegistrationView(FormView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse('items:home')

    def form_valid(self, form):
        form.create_user_and_login(self.request)
        return super().form_valid(form)


class LogoutView(View):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('items:home'))


class LoginView(FormView):
    form_class = UserLoginForm
    success_url = reverse('items:home')
    template_name = 'user/login.html'

    def form_valid(self, form):
        form.login_user(self.request)
        return super().form_valid(form)
