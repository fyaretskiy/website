from django import forms
from django.contrib.auth import authenticate, login

from user.models import User


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def create_user_and_login(self, request):
        data = self.cleaned_data

        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'])
        login(request, user)


class UserLoginForm(forms.Form):

    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput())

    def login_user(self, request):
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            pass
