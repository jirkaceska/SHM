# Generated by Django 3.0.7 on 2020-07-17 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_auto_20200716_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Přiřazeno k'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_set', to=settings.AUTH_USER_MODEL, verbose_name='Autor úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Datum a čas vytvoření'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=2047, verbose_name='Popis úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Konec úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Skupina'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Název úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Začátek úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='super_task',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task', verbose_name='Nadřazený úkol'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_state',
            field=models.CharField(choices=[('NW', 'Nový'), ('IP', 'Probíhá'), ('CO', 'Dokončeno')], default='NW', max_length=2, verbose_name='Stav úkolu'),
        ),
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Tým'),
        ),
        migrations.DeleteModel(
            name='TaskState',
        ),
    ]
