from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Min, Max
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
import pdb

from accounts.models import Profile
from tasks.forms import SignInTaskForm, ApplicationForm, TeamForm, TaskForm, TaskCreateForm
from tasks.models import Application, Task
from utils.utils import get_time_span
from .models import SignableTask
from .forms import CampFilterForm


def camps_list(request):
    tasks = SignableTask.objects.all()

    if request.method == "POST":
        form = CampFilterForm(request.POST)
        leader = request.POST['leader']
        age = request.POST['age']

        if leader != '':
            tasks = tasks.filter(assigned_to=leader)
        if age != '':
            tasks = tasks.filter(age_min__lte=age).filter(age_max__gte=age)
    else:
        form = CampFilterForm()

    return render(request, 'tasks/signabletask_list.html', {
        'tasks': tasks,
        'form': form,
    })


def task_info(request, pk):
    task = SignableTask.objects.get(pk=pk)

    if request.method == 'POST':
        form = SignInTaskForm(request=request)
        child = get_object_or_404(Profile, pk=request.POST['child'])

        if child is not None:
            if Application.objects.filter(person=child, task=task).exists():
                messages.error(request, f'Dítě {child} již bylo přihlášeno na tábor {task}.', 'danger')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.success(request, f'Dítě {child} bylo úspěšně přihlášeno na tábor {task}.')
                application = Application(person=child, task=task)
                application.save()
                return HttpResponseRedirect(request.path_info)

    else:
        form = SignInTaskForm(request=request)

    return render(request, 'tasks/signable_task_info.html', {
        'task': task,
        'form': form
    })


class TaskApplicationsList(LoginRequiredMixin, ListView):
    model = Application

    def get_context_data(self, *, object_list=None, **kwargs):
        pk = self.kwargs['pk']
        task = get_object_or_404(SignableTask, pk=pk)
        applications = Application.objects.filter(task=task)

        return {
            'applications': applications,
            'task': task
        }


class TaskApplicationTasks(LoginRequiredMixin, ListView):
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        pk = self.kwargs['pk']
        task = get_object_or_404(SignableTask, pk=pk)
        unplanned_tasks = Task.objects.filter(super_task=task, start__isnull=True, end__isnull=True)
        planned_tasks = Task.objects.filter(super_task=task, start__isnull=False, end__isnull=False)

        start = planned_tasks.aggregate(Min('start__time'))
        end = planned_tasks.aggregate(Max('end__time'))

        timespan = get_time_span(start, end)

        return {
            'task': task,
            'unplanned_tasks': unplanned_tasks,
            'planned_tasks': planned_tasks,
            'timespan': timespan
        }


def task_team(request, pk):
    task = get_object_or_404(SignableTask, pk=pk)

    if request.method == 'POST':
        form = TeamForm(request.POST)
        user = User.objects.get(pk=request.POST['user'])

        if form.is_valid():
            messages.success(request, f'Animátor {user} byl úspěšně přidán do týmu tábora {task}.')
            task.team.add(user)
            return HttpResponseRedirect(request.path_info)

    else:
        form = TeamForm()

    return render(request, 'tasks/signable_task_team.html', {
        'task': task,
        'form': form,
        'team': task.team.all()
    })


def task_team_delete(request, task_id, user_id):
    task = get_object_or_404(SignableTask, pk=task_id)
    user = get_object_or_404(User, pk=user_id)
    messages.success(request, f'Animátor {user} byl úspěšně odebrán z týmu tábora {task}.', 'danger')
    task.team.remove(user)
    return HttpResponseRedirect(reverse('tasks:taskTeam', args=[task_id]))


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('tasks:taskTasks', args=[self.object.super_task.id])


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse('tasks:taskTasks', args=[self.kwargs['pk']])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created = datetime.now()
        self.object.author = self.request.user
        self.object.task_state = Task.TaskStates.NEW
        self.object.super_task = get_object_or_404(Task, pk=self.kwargs['pk'])

        return super(TaskCreate, self).form_valid(form)


class ApplicationsList(LoginRequiredMixin, ListView):
    model = Application

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.user
        profiles = user.profiles.all()
        applications = Application.objects.filter(person__in=profiles)

        return {
            'applications': applications
        }


class ApplicationSuspend(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('tasks:applications')
    context_object_name = 'application'

    def delete(self, request, *args, **kwargs):
        application = self.get_object()
        application.state = Application.ApplicationStates.SUSPENDED
        application.save()

        return HttpResponseRedirect(self.success_url)


class ApplicationEdit(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('tasks:applications')

    def form_valid(self, form):
        if self.object.state == Application.ApplicationStates.PAID:
            self.object.paid = True
        if self.object.state == Application.ApplicationStates.NON_PAID:
            self.object.paid = False

        return super(ApplicationEdit, self).form_valid(form)
