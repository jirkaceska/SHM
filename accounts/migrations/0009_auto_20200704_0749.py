# Generated by Django 3.0.7 on 2020-07-04 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20200613_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, default='avatar.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(verbose_name='Datum narození'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Město'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Křestní jméno'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='house_number',
            field=models.CharField(max_length=255, verbose_name='Číslo domu'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insurance_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.InsuranceCompany', verbose_name='Pojišťovna'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Příjmení'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='quote',
            field=models.CharField(blank=True, max_length=511, verbose_name='Citát'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=255, verbose_name='Ulice'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=255, verbose_name='PSČ'),
        ),
    ]