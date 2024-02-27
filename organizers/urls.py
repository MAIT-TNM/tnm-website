from django.urls import path
from .views import EventData
urlpatterns = [
	path("data", EventData)
]