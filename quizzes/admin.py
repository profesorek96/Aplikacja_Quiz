from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pytanie,Urzytkownicy

admin.site.register(Pytanie)
admin.site.register(Urzytkownicy)