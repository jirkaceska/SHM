# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Účet {username} byl úspěšně vytvořen!')
            form.save()
            return redirect("/user/login")
    else:
        form = RegisterForm()

    return render(request, "register/../accounts/templates/accounts/register.html", {"form": form})
