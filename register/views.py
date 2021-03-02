from django.shortcuts import render
from core.models import Member
from .forms import *

# Create your views here.


def home(request):
    form = DelegateForm()
    return render(request, 'register/register.html', {'form': form})
