from django.db import models
from .managers import UserManager
from hesabataz.commons import slugify
from django.contrib.auth.models import AbstractUser, BaseUserManager, UnicodeUsernameValidator

class User(AbstractUser):
    COMPANY_CHOICES =(
        ("Hüquqi Şəxs", ("Hüquqi Şəxs")),
        ("Fiziki Şəxs", ("Fiziki Şəxs"))
    )
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        ('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(('email adress'), unique=True, null=True, blank=False)
    is_taxpayer = models.BooleanField(default=False, help_text="")
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    number = models.CharField(max_length=100, null=True, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    has_worker = models.BooleanField(default=False)
    voen_number = models.CharField(max_length=11, null=True, blank=False)
    has_company = models.BooleanField(default=False , help_text="")
    income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expence = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company_type = models.CharField(choices=COMPANY_CHOICES, max_length=50)
    set_time = models.DateTimeField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    passport_number = models.CharField(max_length=100, null=True, blank=True)
    passport_fin = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    voen = models.CharField(max_length=100, null=True, blank=True)
    staff_count = models.IntegerField(null=True, blank=True)
    company_sector = models.CharField(max_length=100, null=True, blank=True)
    bank_rekvizit = models.FileField(upload_to='rekvizits/', null=True, blank=True)
    # birth_date = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        # super(User, self).save(*args, **kwargs)
        if self.first_name and self.last_name:
            self.slug = f'{slugify(self.first_name)}-{slugify(self.last_name)}-{self.email}'
        else:
            self.slug = f"{slugify(self.email)}-{self.id}"
        super(User, self).save(*args, **kwargs)


# class Company(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
#     company_name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     passport_number = models.CharField(max_length=100)
#     passport_fin = models.CharField(max_length=100)
#     birth_date = models.DateTimeField(null=True, blank=True)
#     address = models.CharField(max_length=100)
#     document = models.FileField(upload_to='documents/')
#     voen = models.CharField(max_length=100)
#     staff_count = models.IntegerField()
#     company_sector = models.CharField(max_length=100)
#     bank_rekvizit = models.FileField(upload_to='rekvizits/')

#     class Meta:
#         verbose_name = 'Company'
#         verbose_name_plural = 'Companies'

#     def __str__(self):
#         return f"{self.email}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employes")
    fin = models.CharField(max_length=100, null=True, blank=True)
    monthly_work_hours = models.IntegerField(null=True, blank=True)
    work_hours = models.IntegerField(null=True, blank=True)
    premia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vacation = models.CharField(max_length=100, null=True, blank=True)
    life_insurance = models.CharField(max_length=100, null=True, blank=True)
    income_tax = models.CharField(max_length=100, null=True, blank=True)
    pension_fund = models.CharField(max_length=100, null=True, blank=True)
    unemployment_insurance = models.CharField(max_length=100, null=True, blank=True)
    health_insurance = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkCategory(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'WorkCategory'
        verbose_name_plural = 'WorkCategories'

    def __str__(self):
        return f"{self.title}"


class Income(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.user:
            income = self.user.income
            expence = self.user.expence
            self.user.income = income+self.amount
            self.user.profit = self.user.income-expence
            self.user.save()
        super(Income, self).save(*args, **kwargs)


class Expence(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expences")

    class Meta:
        verbose_name = 'Expence'
        verbose_name_plural = 'Expences'

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.user:
            expence = self.user.expence
            income = self.user.income
            self.user.expence = expence+self.amount
            self.user.profit = income-self.user.expence
            self.user.save()
        super(Expence, self).save(*args, **kwargs)


class Invoice(models.Model):
    full_name = models.CharField(max_length=300)
    voen = models.CharField(max_length=100)
    service = models.CharField(max_length=500)
    note = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f"{self.full_name}'s invoice"