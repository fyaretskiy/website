from django import forms


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
