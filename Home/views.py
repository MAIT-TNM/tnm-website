from django.shortcuts import render,HttpResponse,redirect
from .models import Event
# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        print(request.user)
        events = Event.objects.all().values()
        context = {"events":events,"superuser":request.user.is_superuser}
        return render(request, "Home.html",context=context)
    else:
        return redirect("/Login/")

