from io import BytesIO

from PIL import Image
from django.db import models
from django.contrib.auth.models import User, Group
from stdimage import StdImageField


# Create your models here.
class TaskState(models.Model):
    code = models.CharField(max_length=31)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "<State {}: {}>".format(self.code, self.name)


class Task(models.Model):
    name = models.CharField(max_length=255)
    start = models.DateTimeField(default=None, blank=True, null=True)
    end = models.DateTimeField(default=None, blank=True, null=True)
    description = models.CharField(max_length=2047, blank=True)
    created = models.DateTimeField(default=None, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                                    related_name='assigned_tasks')
    task_state = models.ForeignKey(TaskState, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_set')
    team = models.ManyToManyField(User, blank=True)
    super_task = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return "<Task: {}, Author: {}>".format(self.name, self.author)


class SignableTask(Task):
    start_signing = models.DateTimeField(default=None, blank=True, null=True)
    end_signing = models.DateTimeField(default=None, blank=True, null=True)
    capacity = models.IntegerField()
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    image = StdImageField(upload_to='images', variations={'thumbnail': (100, 100)}, default='logo.png')
    price = models.IntegerField(default=None, blank=True, null=True)
    sponsor_price = models.IntegerField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.sponsor_price or self.sponsor_price < self.price:
            self.sponsor_price = self.price

        super(SignableTask, self).save(*args, **kwargs)

    def __str__(self):
        return "<SignableTask: {}, Author: {}>".format(self.name, self.author)

    def get_date_span(self):
        if self.start is None or self.end is None:
            return None

        start = self.start.date()
        end = self.start.date()

        if start == end:
            return start.strftime('%d. %m. %Y')

        return f'{start.strftime("%d. %m. %Y")} - {end.strftime("%d. %m. %Y")}'

