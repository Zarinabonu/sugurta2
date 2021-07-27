from django.db import models


class Currency(models.Model):
    name = models.TextField(null=True, blank=True)



class Republic(models.Model):
    name = models.TextField(null=True, blank=True)


class City(models.Model):
    republic = models.ForeignKey(Republic, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)


class Region(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)


class District(models.Model):
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)