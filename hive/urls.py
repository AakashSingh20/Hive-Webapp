from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.main, name="main"),
    path('home', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('reader', views.reader, name="reader"),
    path('reader1', views.reader1, name="reader1"),
    path('reader2', views.reader2, name="reader2"),
    path('reader3', views.reader3, name="reader3"),
    path('reader4', views.reader4, name="reader4"),
    path('reader5', views.reader5, name="reader5"),
    path('reader6', views.reader6, name="reader6"),
    path('reader7', views.reader7, name="reader7"),
    path('pdf', views.pdf, name="pdf"),
    path('pdf1', views.pdf1, name="pdf1"),
    path('pdf2', views.pdf2, name="pdf2"),
    path('pdf3', views.pdf3, name="pdf3"),
    path('pdf4', views.pdf4, name="pdf4"),
    path('pdf5', views.pdf5, name="pdf5"),
    path('pdf6', views.pdf6, name="pdf6"),
    path('pdf7', views.pdf7, name="pdf7"),
    path('dev', views.dev, name="dev"),
    path('feedback', views.feedback, name="feedback"),
   

]
