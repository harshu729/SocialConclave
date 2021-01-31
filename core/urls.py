from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('', views.overTheYears, name="overTheYears"),
    path('team/<str:year>/', views.jsonitems, name="core-info"),
    path('agendas/<str:year>/', views.jsonitemsagendas, name="agendas-info")
]
