from django.contrib import admin
import core.models as coremodels

# Register your models here.

admin.site.register(coremodels.Customer)
admin.site.register(coremodels.Event)
admin.site.register(coremodels.Business)
