from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Pytanie,Urzytkownicy

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def start_test(request):
    pytania=Pytanie.objects.all()
    return render(request, "test_arkusz.html",{'pytania':pytania})
