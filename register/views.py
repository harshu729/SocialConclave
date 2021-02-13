from django.shortcuts import render
from core.models import Member

# Create your views here.


def home(request):
    return render(request, 'register/register.html')
