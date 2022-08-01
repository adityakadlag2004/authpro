from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('/login')


def demopage(request):
    return render(request, 'demo.html')


def demoauth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mode = request.POST.get('mode')
        print(username)
        print(password)
        print(mode)
        if mode == 'login':
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'name': username, 'email': email}
                return render(request,'index.html',context)
            else:
                return render(request, 'login.html')
        else:
            email = request.POST.get('email')
            user = User.objects.create_user(username, email, password)
            user.save()

            context = {'name': username, 'email': email}
            login(request, user)
            messages.success(request, 'Profile details Added.')
            return render(request,'index.html',context)

    return render(request, 'demo.html')
