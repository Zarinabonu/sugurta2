from django.db import models

from app.model.classes import DMS, NS, Travel, Bonus, Rent
from app.model.client import Client
from app.model.handbook import Currency, City, Polis
from app.model.employee import Employee


class Class_type(models.Model):
    name = models.TextField(default='', null=True, blank=True)
    code = models.FloatField(null=True,blank=True)


class Payment_type(models.Model):
    name = models.TextField(null=True, blank=True)


class General_information(models.Model):
    OWN = '1'
    BUDGET = '2'
    PAYMENT = (
        (OWN, 'Собсвенные средства '),
        (BUDGET, 'Бюжетные средства'),
    )

    class_type = models.ForeignKey(Class_type, on_delete=models.SET_NULL, null=True)
    date_conclusion = models.DateField(null=True, blank=True)
    start_period = models.DateField(null=True, blank=True)
    finish_period = models.DateField(null=True, blank=True)
    days = models.IntegerField(default='', null=True, blank=True)
    insurer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    currency_condition = models.TextField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    geographic_area = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    contract_number = models.TextField(null=True, blank=True)
    insured_person = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name="insured_person")
    vigod_acquirer = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name="vigod_acquirer")
    payment_source = models.CharField(choices=PAYMENT, null=True, blank=True, max_length=128)
    export_agreement = models.BooleanField(default=False)
    investment_project = models.BooleanField(default=False)
    farmer = models.BooleanField(default=False)
    sez = models.BooleanField(default=False)
    new_client = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)


class Object(models.Model):
    class_type = models.ForeignKey(Class_type, on_delete=models.SET_NULL, null=True)
    dms = models.ForeignKey(DMS, on_delete=models.SET_NULL, null=True)
    ns = models.ForeignKey(NS,on_delete=models.SET_NULL, null=True)
    travel = models.ForeignKey(Travel, on_delete=models.SET_NULL, null=True)
    bonus = models.ForeignKey(Bonus, on_delete=models.SET_NULL, null=True)
    rent = models.ForeignKey(Rent, on_delete=models.SET_NULL, null=True)


class Payment(models.Model):
    date = models.DateField(null=True, blank=True)
    summa = models.FloatField(null=True, blank=True)
    type = models.ForeignKey(Payment_type, on_delete=models.SET_NULL, null=True)
    document_number = models.TextField(null=True, blank=True)
    one_time = models.BooleanField(default=False)
    tranche = models.BooleanField(default=False)


class Polis_insurance(models.Model):
    polis = models.ForeignKey(Polis, on_delete=models.SET_NULL, null=True)


class Contract(models.Model):
    name = models.TextField(null=True, blank=True)


class Portfolio(models.Model):
    general_info = models.OneToOneField(General_information, on_delete=models.CASCADE)
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    polis = models.OneToOneField(Polis, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)

