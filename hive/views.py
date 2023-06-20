from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import FeedBack
# Create your views here.

def main(request):
    return render(request, 'main.html')


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
    
def logout(request):
    return render(request, "main.html")
    

def reader(request):
    return render(request, "reader.html")

def reader1(request):
    return render(request, "reader1.html")

def reader2(request):
    return render(request, "reader2.html")

def reader3(request):
    return render(request, "reader3.html")

def reader4(request):
    return render(request, "reader4.html")

def reader5(request):
    return render(request, "reader5.html")

def reader6(request):
    return render(request, "reader6.html")

def reader7(request):
    return render(request, "reader7.html")


def pdf(request):
    return render(request, 'pdf.html')

def pdf1(request):
    return render(request, 'pdf1.html')

def pdf2(request):
    return render(request, 'pdf2.html')

def pdf3(request):
    return render(request, 'pdf3.html')

def pdf4(request):
    return render(request, 'pdf4.html')

def pdf5(request):
    return render(request, 'pdf5.html')

def pdf6(request):
    return render(request, 'pdf6.html')

def pdf7(request):
    return render(request, 'pdf7.html')

def dev(request):
    return render(request, 'OurTeamPage.html')

def feedback(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        en = FeedBack(name= name, email= email, contact= contact, message=message)
        en.save()
        return redirect('/home')


    return render(request, 'feedback.html')

