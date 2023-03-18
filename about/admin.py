from django.contrib import admin
from .models import Employee, Timeline, Privacy, Terms 

# Register your models here.
admin.site.register([Employee, Timeline, Privacy, Terms])