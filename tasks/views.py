from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
import pdb

from .models import SignableTask
from .forms import CampFilter


def camps_list(request):
    tasks = SignableTask.objects.all()

    if request.method == "POST":
        form = CampFilter(request.POST)
        leader = request.POST['leader']
        age = request.POST['age']

        if leader != '':
            tasks = tasks.filter(assigned_to=leader)
        if age != '':
            tasks = tasks.filter(age_min__lte=age).filter(age_max__gte=age)
    else:
        form = CampFilter()

    return render(request, 'tasks/signabletask_list.html', {
        'tasks': tasks,
        'form': form,
    })


class TaskDetail(DetailView):
    model = SignableTask
    template_name = 'tasks/signabletask_detail.html'
    context_object_name = 'task'
