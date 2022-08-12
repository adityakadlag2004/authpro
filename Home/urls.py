from django import views
from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('logout',views.logout_view,name="logout"),
    path('login',views.demoauth,name="demologin"),
    path('about',views.index,name="about"),
    path('contact',views.contact,name="contact"),
    path('tracker',views.tracker,name="tracker"),
    path('products/<int:myid>',views.productView,name="product"),
    path('checkout',views.checkout,name="checkout"),
]
