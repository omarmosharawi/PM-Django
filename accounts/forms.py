from django.contrib.auth.forms import AuthenticationForm
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