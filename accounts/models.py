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
    email = models.EmailField(('email adress'), unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    has_company = models.BooleanField(default=False)
    company_type = models.CharField(choices=COMPANY_CHOICES, max_length=50)
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