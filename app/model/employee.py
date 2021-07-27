from django.contrib.auth.models import User
from django.db import models

from app.model.company import Company, Company_branch


class Employee(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.TextField()
    # password = models.TextField()
    ONLY_YOURS = 'only_yours'
    SUBDIVISION = 'subdivision'
    BRANCHES = 'branches'
    ALL_BRANCHES = 'all_branches'
    CONTRACT = (
        (ONLY_YOURS, 'только своим'),
        (SUBDIVISION, 'подразделение'),
        (BRANCHES, 'филиалы'),
        (ALL_BRANCHES, 'всех филиалов'),
    )

    CREATE_UPDATE = 'create_update'
    ONLY_READ = 'only_read'
    ONLY_READ_OWN_CREATE = 'only_read_own_create'
    PERMISSION = (
        (CREATE_UPDATE, 'Cоздание/редактирование договора '),
        (ONLY_READ, 'Только для читение '),
        (ONLY_READ_OWN_CREATE, 'Только для читение/созд.своих '),
    )

    NO = 'no'
    USER = 'user'
    ADMINISTRATOR = 'administrator'
    CHECKING = (
        (NO, 'Нет'),
        (USER, 'Пользователь'),
        (ADMINISTRATOR, 'Администратор'),
    )

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_branch = models.ForeignKey(Company_branch, on_delete=models.CASCADE)
    login = models.TextField()
    password = models.TextField()
    act_start_date = models.DateField()
    act_finish_date = models.DateField()
    reference = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    insurer = models.BooleanField(default=False)
    access_contract_type = models.CharField(choices=CONTRACT,  null=True, blank=True, max_length=128)
    access_permission_type = models.CharField(choices=PERMISSION,  null=True, blank=True, max_length=128)
    pretense = models.BooleanField(default=False)
    library = models.BooleanField(default=False)
    update_news = models.BooleanField(default=False)
    checking = models.CharField(choices=CHECKING,  null=True, blank=True, max_length=128)
    import_data = models.BooleanField(default=False)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    fath_name = models.TextField(null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    passport_serial = models.CharField(null=True, blank=True, max_length=9)
    given_date = models.DateField(null=True, blank=True)
    issue_place = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)