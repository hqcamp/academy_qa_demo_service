from django.contrib import admin
from demo_service.models import Pet
from demo_service.models import PetCategory

admin.site.register(Pet)
admin.site.register(PetCategory)