# Generated by Django 3.0.7 on 2020-06-13 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_code', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.InsuranceCompany')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.InsuranceCompany')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
