from django.contrib import admin
from .models import Employee, Timeline, Privacy, Term

# Register your models here.
admin.site.register([Employee, Timeline, Privacy, Term])