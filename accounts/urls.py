from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm, UserRegisterForm
from .views import RegisterView, ProfileForm, edit_profile

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('profile/', edit_profile, name='Profile'),
    path('', include('django.contrib.auth.urls')),
]