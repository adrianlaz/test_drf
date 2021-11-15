from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

router.register(r'country', views.CountryViewSet)
router.register(r'county', views.CountyViewSet)
router.register(r'city', views.CityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]