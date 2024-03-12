from django.urls import path
from .views import paymenthandler, pay
urlpatterns = [
    path("Pay/<name>/", pay, name='register'),
    path('paymenthandler/<name>', paymenthandler, name='paymenthandler'),
    # path('Regi', Regi)
]