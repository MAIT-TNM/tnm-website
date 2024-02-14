from django.urls import path
from .views import paymenthandler, pay
urlpatterns = [
    path("Register/<name>", pay, name='register'),
    path('paymenthandler/<name>', paymenthandler, name='paymenthandler'),
]