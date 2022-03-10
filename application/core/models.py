from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)



class County(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='counties', on_delete=models.CASCADE)



class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
