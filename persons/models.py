from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    additional_countries = models.ManyToManyField(Country, related_name="eyo", blank=True, null=True)
    city = models.ManyToManyField(City, blank=True, null=True)

    def __str__(self):
        return self.name