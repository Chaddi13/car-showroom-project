from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator


class IsActive(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Info(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    country = CountryField(multiple=True)

    class Meta:
        abstract = True


class Discount(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount_of_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        abstract = True
