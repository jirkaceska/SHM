# Generated by Django 3.0.7 on 2020-06-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200613_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='quote',
            field=models.CharField(blank=True, max_length=511),
        ),
    ]
