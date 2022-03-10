from rest_framework import serializers

from core.models import Country, County, City


class CountrySerializer(serializers.ModelSerializer):
    counties = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'counties']


class CountySerializer(serializers.ModelSerializer):
    cities = serializers.StringRelatedField(many=True)

    class Meta:
        model = County
        fields = ['id',  'cities']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'county']