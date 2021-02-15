from django.shortcuts import render
from core.models import Member

# Create your views here.


def home(request):
    depts = [i['deptName'] for i in Member.objects.values(
        'deptName').order_by('deptName').distinct()]
    return render(request, 'main/index.html', {'depts': depts})


def ayushya(request):
    return render(request, 'main/blogs.html')
