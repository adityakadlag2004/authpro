from django import views
from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('logout',views.logout_view,name="logout"),
    path('login',views.demoauth,name="demologin"),
    path('about',views.index,name="demologin"),
    path('contact',views.contact,name="demologin"),
    path('tracker',views.tracker,name="demologin"),
    path('productview',views.productview,name="demologin"),
    path('checkout',views.checkout,name="demologin"),
]
