from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home/home.html")

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dang ki thanh cong")
    context = {
        'form':form
    }
    return render(request,"home/signup.html",context)

def signin(request):
    user_name = ''
    pass_word = ''

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        is_auth = authenticate(username = user_name,password = pass_word)
        if is_auth:
            login(request, is_auth)
      
            return redirect('home:home')
    
    return render(request,"home/signin.html")

def logout2(request):

    logout(request)
    return redirect("home:signin")