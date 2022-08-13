from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {
        'allProds': allProds,
    }
    return render(request, 'shop/index.html', params)


def search(request):
    if request.method == 'GET':
        print(request)
        product_nm = request.GET.get('search_item', '')
        print(product_nm)
        prod=None
        prod = Product.objects.filter(productName=product_nm)
        if prod[0] is not None:
            return render(request, 'shop/search.html',{"product":prod[0]})    
    print("Redirect")
    return redirect('shop/index.html')

    


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def productView(request, myId):
    product = Product.objects.filter(id=myId)
    print(product)
    return render(request, 'shop/prodview.html', {'product': product[0]})


def tracker(request):
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                      state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank,'id':id})

    return render(request, 'shop/checkout.html')
