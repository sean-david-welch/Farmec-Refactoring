from django.contrib import admin
from .models import SupplierPage, PartsPage, WarrantyClaim, PartsRequired, MachineRegistration

# Register your models here.
admin.site.register(SupplierPage)
admin.site.register(PartsPage)
admin.site.register(WarrantyClaim)
admin.site.register(PartsRequired)
admin.site.register(MachineRegistration)

