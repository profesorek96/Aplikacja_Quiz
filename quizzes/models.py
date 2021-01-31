from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from rest_framework import serializers, viewsets

class Pytanie(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tresc=models.TextField()
    odp_A=models.CharField(max_length=200)
    odp_B = models.CharField(max_length=200)
    odp_C = models.CharField(max_length=200)
    odp_D = models.CharField(max_length=200)
    odp_poprawna=models.CharField(max_length=200)
    # class Meta:
    #     db_table = 'book'
    #     verbose_name = 'Book'
    #     verbose_name_plural = 'Books'
    # def __unicode__(self):
    #     return self.title
    # def __str__(self):
    #     return self.title

# # Serializers define the API representation.
# class PytanieSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pytanie
#         fields = ['tresc', 'odp_A', 'odp_B', 'odp_C','odp_D']
#
# # ViewSets define the view behavior.
# class PytaniaViewSet(viewsets.ModelViewSet):
#     queryset = Pytanie.objects.all()
#     serializer_class = PytanieSerializer

class Urzytkownicy(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    liczba_punktow=models.IntegerField()