from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from shop.models import Company


def company_logo_directory(instance, filename):
    return f'{instance.name}/logos/{filename}'


class User(AbstractUser):
    USER_ROLES = (
        ('user', 'user'),
        ('employee', 'employee'),
    )
    role = models.CharField(
        choices=USER_ROLES, 
        max_length=10
    )


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    company= models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='employees'
    )
    phone_number = models.CharField(
        max_length=25,
        blank=True, null=True
    )
    photo = models.ImageField(
        upload_to=company_logo_directory,
        blank=True, null=True
    )

    class Meta:
        db_table = 'employee'
        verbose_name_plural = "Работники компании"
    
    def __str__(self):
        return f'{self.user}\n{self.company}\n{self.phone_number}'

