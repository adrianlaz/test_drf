from django_filters import rest_framework as filters


from core.models import Country, County, City


# class CountryFilter(filters.FilterSet):
#     class Meta:
#         model = Country
#         fields = {
#             'id': ['exact'],
#             'name': ['icontains'],
#             'code': ['exact'],
#         }

class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    code = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Country
        fields = ['id']


class CountyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    country = filters.ModelChoiceFilter(to_field_name='name__icontains', queryset=Country.objects.all())

    class Meta:
        model = County
        fields = ['id']


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    county = filters.ModelChoiceFilter(to_field_name='name__icontains', queryset=County.objects.all())
    country = filters.ModelChoiceFilter(field_name='county__country',  to_field_name='name__icontains', queryset=Country.objects.all())

    class Meta:
        model = City
        fields = ['id']

