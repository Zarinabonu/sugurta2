from django.db import models


class Company(models.Model):
    name = models.TextField()


class Company_branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.TextField()