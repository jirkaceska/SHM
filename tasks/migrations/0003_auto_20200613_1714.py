# Generated by Django 3.0.7 on 2020-06-13 17:14

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_signabletask_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signabletask',
            name='image',
            field=stdimage.models.StdImageField(default='camp.png', upload_to='images'),
        ),
    ]
