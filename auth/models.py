from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone

from .managers import CustomUserManager

class Register(AbstractUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Username',
        max_length=255,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Email',
        null=True,
        blank=True
    )
    full_name = models.CharField(
        verbose_name='Full name',
        null=True,
        blank=True
    )
    password = models.CharField(
        max_length=100
    )

    is_active = models.BooleanField(
        'is_active',
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_superuser = models.BooleanField(
        'superuser',
        default=False,
        help_text=('Superuser can get access to admin page')
    )
    last_login = models.DecimalField('last login', blank=True, null=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now())

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'full_name'
        'password'
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

