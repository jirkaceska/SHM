from django.contrib import admin

# Register your models here.
from .models import Profile, InsuranceCompany

admin.site.register(Profile)
admin.site.register(InsuranceCompany)
