# Generated by Django 3.0.7 on 2020-06-13 17:09

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200613_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=stdimage.models.StdImageField(default='avatar.png', upload_to='images'),
        ),
    ]
