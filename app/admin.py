from django.contrib import admin
from .models import District, DMS, Individual, NS, Travel, Contract,\
    City,Class_type,General_information,Payment_type,Payment,Object,Portfolio, Polis_insurance,\
    Rent,Client, Region, Company_branch, Currency, Company, Loyal, Polis, Bonus, Okonx, Employee


admin.site.register(District)
admin.site.register(DMS)
admin.site.register(Individual)
admin.site.register(NS)
admin.site.register(Travel)
admin.site.register(Contract)
admin.site.register(City)
admin.site.register(Company_branch)
admin.site.register(Class_type)
admin.site.register(General_information)
admin.site.register(Payment_type)
admin.site.register(Payment)
admin.site.register(Object)
admin.site.register(Portfolio)
admin.site.register(Rent)
admin.site.register(Client)
admin.site.register(Region)
admin.site.register(Currency)
admin.site.register(Company)
admin.site.register(Loyal)
admin.site.register(Polis)
admin.site.register(Bonus)
admin.site.register(Okonx)
admin.site.register(Employee)
admin.site.register(Polis_insurance)


# Register your models here.
