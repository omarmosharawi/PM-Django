from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
]