from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _

attributes = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attributes)
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=attributes)
    )


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs=attributes)
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs=attributes)
    )
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attributes)
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs=attributes)
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=attributes)
    )
    password2 = forms.CharField(
        label=_('Password Confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs=attributes)
    )

    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attributes),
            'last_name': forms.TextInput(attrs=attributes),
            'email': forms.EmailInput(attrs=attributes),
        }