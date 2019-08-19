from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pantry

def home(request):
    pantries = Pantry.objects.all()
    return render(request, 'home.html', {'pantries': pantries})

def pantry_detail(request, id):
    try:
        pantry = Pantry.objects.get(id=id)
    except Pantry.DoesNotExist:
        raise Http404('Pantry not found')
    return render(request, 'pantry_detail.html', {'pantry': pantry})
