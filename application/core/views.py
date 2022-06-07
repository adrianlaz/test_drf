from rest_framework import viewsets

# Create your views here.
from core.filters import CountryFilter, CountyFilter, CityFilter
from core.models import Country, County, City
from core.serializers import CountrySerializer, CountySerializer, CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filterset_class = CountryFilter


class CountyViewSet(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    filterset_class = CountyFilter
    lookup_field = 'pk'
    test_field = None


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    try:
        filterset_class = CityFilter
    except IndexError:
        pass