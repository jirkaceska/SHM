from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import ModelFormMixin, ProcessFormView

from accounts.forms import RegisterForm, ProfileForm, ChildForm

# Create your views here.
from accounts.models import Profile


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Účet {username} byl úspěšně vytvořen!')
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})


class AccountDetail(DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user = super(AccountDetail, self).get_object(queryset=queryset)
        profile = user.get_profile()
        return profile


class AccountsList(ListView):
    model = Profile
    template_name = 'user/list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return super(AccountsList, self).get_queryset()\
            .filter(primary_profile=True)


class ProfileView(LoginRequiredMixin, ModelFormMixin, ProcessFormView):
    model = Profile
    form_class = ProfileForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        request = self.request
        username = request.user.username
        messages.success(request, f'Účet {username} byl úspěšně změněn!')
        return super(ProfileView, self).form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Pro správu profilu musíte být přihlášeni!', 'danger')
        return super(ProfileView, self).handle_no_permission()


class ProfileEdit(UpdateView, ProfileView):

    def get_object(self, queryset=None):
        user = self.request.user
        return user.get_profile()


class ProfileCreate(CreateView, ProfileView):

    # def __init__(self):
    #     self.object = None
    #     super(ProfileCreate, self).__init__()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.primary_profile = True

        return super(ProfileCreate, self).form_valid(form)


# def choose_profile_view(request):
#     if request.user.has_profile():
#         return ProfileEdit()
#     return ProfileCreate()


class ChildrenCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ChildForm
    success_url = reverse_lazy('accounts:children')

    # def __init__(self):
    #     self.object = None
    #     super(ChildrenCreate, self).__init__()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.primary_profile = False

        return super(ChildrenCreate, self).form_valid(form)

    def get_initial(self):
        self.initial.update({'profile': self.request.user.get_profile()})
        return super(ChildrenCreate, self).get_initial()


class ChildrenList(LoginRequiredMixin, ListView):
    model = Profile

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.user
        return {
            'children': user.get_children()
        }


class ChildDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('accounts:children')
    context_object_name = 'child'


class ChildEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ChildForm
    success_url = reverse_lazy('accounts:children')
