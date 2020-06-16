from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from stdimage import StdImageField


class InsuranceCompany(models.Model):
    insurance_code = models.IntegerField()
    name = models.CharField(max_length=255)


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.PROTECT)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    primary_profile = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    avatar = StdImageField(upload_to='images', variations={'thumbnail': (100, 100)}, default='avatar.png')
    quote = models.CharField(max_length=511, blank=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_address(self):
        return f'{self.street} {self.house_number}, {self.zip_code} {self.city}'

    def __str__(self):
        return f'<Profile: {self.get_full_name()}'
