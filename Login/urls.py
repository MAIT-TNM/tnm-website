from django.urls import path
from .views import *
urlpatterns = [
    path("Signup/", SignUp, name='signup'),
    path("Login/", Login, name='login'),
    path("Logout/", Logout, name='logout'),
    path("SignupAPI/", SignUpAPI.as_view())
]