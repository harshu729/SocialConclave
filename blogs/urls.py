from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.home, name="blogs-home"),
    path('<str:blog>',views.blogview,name="blog-view"),
]
