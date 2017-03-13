from django.views.generic.edit import FormView, CreateView
from django.shortcuts import reverse
from .forms import UserRegistrationForm
from .models import User


class UserRegistrationView(FormView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse('items:home')

    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(username=data['username'],
                                 email=data['email'],
                                 password=data['password'])

        super().form_valid(form)
