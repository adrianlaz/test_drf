from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core import views

router = SimpleRouter()

router.register(r'country', views.CountryViewSet)
router.register(r'county', views.CountyViewSet)
router.register(r'city', views.CityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]