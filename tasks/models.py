from io import BytesIO

from PIL import Image
from django.db import models
from django.contrib.auth.models import User, Group
from stdimage import StdImageField


# Create your models here.
from accounts.models import Profile


# class TaskState(models.Model):
#     code = models.CharField(max_length=31)
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Task(models.Model):
    class TaskStates(models.TextChoices):
        NEW = 'NW', 'Nový'
        IN_PROGRESS = 'IP', 'Probíhá'
        COMPLETED = 'CO', 'Dokončeno'

    name = models.CharField(max_length=255, verbose_name="Název úkolu")
    start = models.DateTimeField(default=None, blank=True, null=True, verbose_name="Začátek úkolu")
    end = models.DateTimeField(default=None, blank=True, null=True, verbose_name="Konec úkolu")
    description = models.CharField(max_length=2047, blank=True, verbose_name="Popis úkolu")
    created = models.DateTimeField(default=None, blank=True, null=True, verbose_name="Datum a čas vytvoření")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                              verbose_name="Skupina")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                                    related_name='assigned_tasks', verbose_name="Přiřazeno k")
    task_state = models.CharField(
        max_length=2,
        choices=TaskStates.choices,
        default=TaskStates.NEW,
        verbose_name='Stav úkolu'
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_set', verbose_name="Autor úkolu")
    team = models.ManyToManyField(User, blank=True, verbose_name="Tým")
    super_task = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True,
                                   verbose_name="Nadřazený úkol")

    def __str__(self):
        return "Úkol: {}".format(self.name)

    def get_color(self):
        if self.task_state == self.TaskStates.NEW:
            return 'primary'
        elif self.task_state == self.TaskStates.IN_PROGRESS:
            return 'warning'
        elif self.task_state == self.TaskStates.COMPLETED:
            return 'success'


class SignableTask(Task):
    start_signing = models.DateTimeField(default=None, blank=True, null=True)
    end_signing = models.DateTimeField(default=None, blank=True, null=True)
    capacity = models.IntegerField()
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    image = StdImageField(upload_to='images', variations={'thumbnail': (100, 100)}, default='logo.png')
    price = models.IntegerField(default=None, blank=True, null=True)
    sponsor_price = models.IntegerField(default=None, blank=True, null=True)
    applications = models.ManyToManyField(Profile, through='Application', related_name='applications')

    def save(self, *args, **kwargs):
        if not self.sponsor_price or self.sponsor_price < self.price:
            self.sponsor_price = self.price

        super(SignableTask, self).save(*args, **kwargs)

    def __str__(self):
        return "Akce: {}".format(self.name)

    def get_date_span(self):
        if self.start is None or self.end is None:
            return None

        start = self.start.date()
        end = self.start.date()

        if start == end:
            return start.strftime('%d. %m. %Y')

        return f'{start.strftime("%d. %m. %Y")} - {end.strftime("%d. %m. %Y")}'

    def get_age_span(self):
        return f'{self.age_min} - {self.age_max}'

    def get_vacancies(self):
        return self.capacity - Application.objects.filter(task=self).count()


class Application(models.Model):
    class ApplicationStates(models.TextChoices):
        NON_PAID = 'NP', 'Nezaplaceno'
        PAID = 'PA', 'Zaplaceno'
        SUSPENDED = 'SU', 'Zažádáno o zrušení'

    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(SignableTask, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    state = models.CharField(
        max_length=2,
        choices=ApplicationStates.choices,
        default=ApplicationStates.NON_PAID,
        verbose_name='Stav'
    )

    def __str__(self):
        return "Přihláška: {} na tábor {}".format(self.person, self.task)

    def get_color(self):
        if self.state == self.ApplicationStates.NON_PAID:
            return 'danger'
        elif self.state == self.ApplicationStates.PAID:
            return 'success'
        elif self.state == self.ApplicationStates.SUSPENDED:
            return 'warning'

    def is_suspended(self):
        return self.state == self.ApplicationStates.SUSPENDED


