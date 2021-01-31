from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Member, Agenda
import json
app_name = "core"


def jsonitems(request, year):
    coreinfo = serializers.serialize("json", Member.objects.all().filter(
        year__icontains=year).order_by('posnum', 'firstName'))
    coreinfo = json.loads(coreinfo)
    return JsonResponse(coreinfo, safe=False)


def jsonitemsagendas(request, year):
    agendasinfo = serializers.serialize(
        "json", Agenda.objects.all().filter(
            year__icontains=year).order_by('title'))
    agendasinfo = json.loads(agendasinfo)
    return JsonResponse(agendasinfo, safe=False)


def overTheYears(request):
    return render(request, 'core/overTheYears.html')
