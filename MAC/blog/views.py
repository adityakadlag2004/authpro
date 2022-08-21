from django.shortcuts import render
from .models import Blogpost


def index(request):
    blogs = Blogpost.objects.all()
    print("length = ",blogs)
    return render(request, 'blog/index.html',{"blogs":blogs})


def BlogPost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,"blog/Blogpost.html",{"post":post})