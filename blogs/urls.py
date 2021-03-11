from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blogs"

urlpatterns = [
    path('<str:blogslug>/', views.eachblog, name="eachblog"),
]
