from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm,LoginForm
from .models import NewUser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView, Response
from .serialzer import UserSerializer


# Create your views here.
def SignUp(request):
    if request.method == "GET":
        context = {}
        context['form'] = SignUpForm()
        return render(request, 'Signup.html', context=context)
    elif request.method == "POST":
        login_form = SignUpForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            try:
                user = NewUser.objects.create_user(email=data["email"], phone=data["phone"], password=data["password"])
                user.save()
                send_mail(
                    "TnM Registration",
                    "hello user you have reistered for MAIT TnM"
                    "welcome to the experience ",
                    settings.EMAIL_HOST_USER,
                    [data["email"]],
                    fail_silently=False,
                )
            except Exception as e:
                print(e)
        return redirect("https://google.com")

def Login(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(email=data["email"], password=data["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect('/Login/')
    else:
        if request.user.is_authenticated:
            return redirect("")
        context = {}
        context['form'] = LoginForm
        return render(request,'Login.html', context)

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/Login/")


class SignUpAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serialised = UserSerializer(data=data)
        if serialised.is_valid():
            print(serialised.validated_data)
            serialised.save()
        return HttpResponse("hello")

