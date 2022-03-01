from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Already taken")
                print("Username Already taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already taken")
                print("Email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email)
                user.save()
                print("user created successfully")
                return redirect('login')

        else:
            print("password do not match")
            messages.info(request, "passwords do not match")
            return redirect('register')
        return redirect('')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

