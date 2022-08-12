from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Contact, Product
from math import ceil


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'index.html', params)


# Create your views here.
def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")


# Create your views here.
def tracker(request_tra):
    return render(request_tra, 'tracker.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "prodView.html", {'product': product[0]})


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
                return render(request, 'demo.html')
        else:
            email = request.POST.get('email')
            user = User.objects.create_user(username, email, password)
            user.save()
            context = {'name': username, 'email': email}
            login(request, user)
            messages.success(request, 'Profile details Added.')
            return redirect('/', context)

    return render(request, 'demo.html')
