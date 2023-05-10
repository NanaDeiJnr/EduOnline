from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Profile, Course
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password_2']

        if password == password_2:                                          #Check Passwords
            if User.objects.filter(email=email).exists():                     #Check if email is already in use
                messages.info(request, 'Email is already in use')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords must be the same')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:                        #Check if user exists in database or not
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid user credentials')
            return redirect('login')
    else:
        return render(request, 'signin.html')

@login_required(login_url='login')
def home(request):
    course = Course.objects.all()
    return render(request, 'home.html', {'course': course})

def courses(request):
    course = Course.objects.all()
    return render(request, 'courses.html', {'course': course})