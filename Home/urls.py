from django.urls import path
from .views import *
urlpatterns = [
    path("", Home, name="Home"),
    path("test/", HomeAPI.as_view()),
    path("registerapi/", RegisterAPI.as_view())
]