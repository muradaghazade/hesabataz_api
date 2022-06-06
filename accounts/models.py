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
    company_type = models.CharField(choices=COMPANY_CHOICES, max_length=50)
    set_time = models.DateTimeField()
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
        super(User, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.first_name)}-{slugify(self.last_name)}-{self.id}'
        super(User, self).save(*args, **kwargs)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    company_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    passport_fin = models.CharField(max_length=100)
    birth_date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    voen = models.CharField(max_length=100)
    staff_count = models.IntegerField()
    company_sector = models.CharField(max_length=100)
    bank_rekvizit = models.FileField(upload_to='rekvizits/')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expences = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.email}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"