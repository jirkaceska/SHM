from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User

from accounts.forms import ChildForm
from accounts.models import Profile
from tasks.models import Application, Task


class CampFilterForm(forms.Form):
    age = forms.IntegerField(required=False, label="Věk:")
    leader = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Hlavní vedoucí:")
    # TODO: Filter only leaders


class SignInTaskForm(forms.Form):
    child = forms.ModelChoiceField(queryset=Profile.objects.none(), required=True, label="Přihlásit dítě:",
                                   empty_label="---")

    def __init__(self, request, *args, **kwargs):
        super(SignInTaskForm, self).__init__(*args, **kwargs)
        if request.user.is_authenticated:
            self.fields['child'].queryset = request.user.get_children()


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["state"]

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.child_form = ChildForm(instance=self.instance and self.instance.person)

        for field in self.child_form.fields:
            self.child_form.fields[field].disabled = True
        # widgets = {
        #     'name': forms.TextInput(attrs={'disabled': True}),
        # }


class TeamForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, label="Přidat animátora:")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["created", "author", "team", "super_task"]


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["created", "author", "team", "super_task", "task_state"]
