from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from core.models import Country, County, City
from core.serializers import CountrySerializer, CountySerializer, CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CountyViewSet(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
