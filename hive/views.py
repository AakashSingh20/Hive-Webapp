from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):
    return render(request, 'Home.html')

def signin(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')

        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/signin')

    else:
        return render(request, "signin.html")

def signup(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email= request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('/signup')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already in use")
            return redirect('/signup')

        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            # print("user created")
            return redirect('/signin')


    else:
        return render(request, "signup.html")