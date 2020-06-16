from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import DetailView, ListView

from accounts.forms import RegisterForm


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
