from django.db import models
from django.utils.translation import gettext_lazy as _


class PetCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pet(models.Model):
    class PetStatus(models.TextChoices):
        AVAILABLE = "available", _("Available")
        PENDING = "pending", _("Pending")
        SOLD = "sold", _("Sold")

    name = models.CharField(max_length=150, unique=True)
    photo_url = models.CharField(max_length=150)
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30,
        choices=PetStatus.choices,
        default=PetStatus.AVAILABLE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
