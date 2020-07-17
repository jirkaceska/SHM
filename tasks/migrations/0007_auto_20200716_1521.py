# Generated by Django 3.0.7 on 2020-07-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200704_0749'),
        ('tasks', '0006_auto_20200716_1516'),
    ]

    operations = [
	migrations.RemoveField(
	    model_name='signabletask',
	    name='applications',
	),
        migrations.AddField(
            model_name='signabletask',
            name='applications',
            field=models.ManyToManyField(through='tasks.Application', to='accounts.Profile'),
        ),
    ]
