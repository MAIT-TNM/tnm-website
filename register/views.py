from django.shortcuts import render,HttpResponse
from Home.models import Event, Participation
from Login.models import NewUser
# Create your views here.
def register(request, name):
    event = Event.objects.get(event_name=name)
    user = NewUser.objects.get(email=request.user)
    registration = Participation(particpant_email=user, event=event,phone=user.phone)
    registration.save()
    return HttpResponse("hello")