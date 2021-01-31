from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Pytanie(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tresc=models.TextField()
    odp_A=models.CharField(max_length=200)
    odp_B = models.CharField(max_length=200)
    odp_C = models.CharField(max_length=200)
    odp_D = models.CharField(max_length=200)
    odp_poprawna=models.CharField(max_length=200)


class Urzytkownicy(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    liczba_punktow=models.IntegerField()