from django.contrib import admin
from .models import Business

class BusinessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Business, BusinessAdmin)
