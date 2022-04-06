from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        login(request, user)
        subject = 'Welcome to the SendMail App'
        message = f"Hi {user.username}, thank you for registering for our SendMail App service"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect("/home")

    
    return render(request, 'signup.html')