from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from stdimage import StdImageField


class InsuranceCompany(models.Model):
    insurance_code = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Křestní jméno")
    last_name = models.CharField(max_length=255, verbose_name="Příjmení")
    phone = models.CharField(max_length=255, verbose_name="Telefon")
    birth_date = models.DateField(verbose_name="Datum narození")
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.PROTECT, verbose_name="Pojišťovna")
    street = models.CharField(max_length=255, verbose_name="Ulice")
    house_number = models.CharField(max_length=255, verbose_name="Číslo domu")
    city = models.CharField(max_length=255, verbose_name="Město")
    zip_code = models.CharField(max_length=255, verbose_name="PSČ")

    primary_profile = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    avatar = StdImageField(upload_to='images', variations={'thumbnail': (100, 100)}, default='avatar.png', blank=True)
    quote = models.CharField(max_length=511, blank=True, verbose_name="Citát")

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_address(self):
        return f'{self.street} {self.house_number}, {self.zip_code} {self.city}'

    def __str__(self):
        return f'<Profile: {self.get_full_name()}'
