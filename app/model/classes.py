from django.db import models


class DMS(models.Model):
    oked = models.IntegerField(null=True, blank=True)
    activity_type = models.TextField(null=True, blank=True)
    summa_by_contract = models.FloatField(null=True, blank=True)
    tariff = models.FloatField(null=True, blank=True)
    jurnal_register_number = models.TextField(null=True, blank=True)
    register_date = models.DateField(null=True, blank=True)


class Rent(models.Model):
    sum_by_contract = models.FloatField(null=True, blank=True)
    year_rent_sum = models.IntegerField(null=True, blank=True)
    rent_till60 = models.DateField(null=True, blank=True)
    n1 = models.FloatField(null=True, blank=True)
    n2 = models.FloatField(null=True, blank=True)
    rent2_till60 = models.DateField(null=True, blank=True)
    premium = models.FloatField(null=True, blank=True)
    start_period = models.DateField(null=True, blank=True)
    jurnal_register_number = models.TextField(null=True, blank=True)
    register_date = models.DateField(null=True, blank=True)


class Rent_payment(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    summa = models.FloatField(null=True, blank=True)


class Bonus(models.Model):
    pre_death = models.TextField(null=True, blank=True)
    pre_live = models.TextField(null=True, blank=True)
    payment_from_contract = models.FloatField(null=True, blank=True)
    monthly_payment = models.FloatField(null=True, blank=True)
    tariff = models.FloatField(null=True, blank=True)
    jurnal_register_number = models.TextField(null=True, blank=True)
    register_date = models.DateField(null=True, blank=True)


class Travel(models.Model):
    name = models.TextField(null=True, blank=True)


class NS(models.Model):
    oked = models.IntegerField(null=True, blank=True)
    activity_type = models.TextField(null=True, blank=True)
    summa_by_contract = models.FloatField(null=True, blank=True)
    tariff = models.FloatField(null=True, blank=True)
    jurnal_register_number = models.TextField(null=True, blank=True)
    register_date = models.DateField(null=True, blank=True)
