from locale import currency
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    """Custom User Model"""

    # GENDER
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    # LANGUAGE
    LANGUAGE_CHOICES = [
        ("kr", "Korean"),
        ("en", "English"),
    ]

    # CURRENCY
    CURRENCY_CHOICES = [
        ("usd", "USD"),
        ("krw", "KRW"),
    ]

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=GENDER_CHOICES
    )
    birthday = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, blank=True, null=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, null=True, blank=True, max_length=10
    )
    superhost = models.BooleanField(default=False)
