from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Product
from math import ceil


# Create your views here.
def index(request_ind):
    if request_ind.user.is_anonymous:
        return redirect('/login')
    products = Product.objects.all()
    n = len(products)
    print("No of Products : ", n)
    no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
    all_prods = [[products, range(1, no_of_slides), no_of_slides], [products, range(1, no_of_slides), no_of_slides]]
    params = {"all_prods": all_prods}
    return render(request_ind, 'index.html', params)


# Create your views here.
def contact(request_con):
    if request_con.user.is_anonymous:
        return redirect('/login')
    return render(request_con, 'contact.html')


# Create your views here.
def tracker(request_tra):
    return render(request_tra, 'tracker.html')


# Create your views here.
def productview(request_pr_view):
    return render(request_pr_view, 'productview.html')


# Create your views here.
def checkout(request_checkout):
    return render(request_checkout, 'checkout.html')


def logout_view(request):
    logout(request)
    return redirect('/login')


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
                return redirect('/', context)
            else:
                return render(request, 'login.html')
        else:
            email = request.POST.get('email')
            user = User.objects.create_user(username, email, password)
            user.save()
            context = {'name': username, 'email': email}
            login(request, user)
            messages.success(request, 'Profile details Added.')
            return redirect('/', context)

    return render(request, 'demo.html')
