from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from accounts.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['primary_profile', 'owner']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['primary_profile', 'owner', 'avatar', 'quote']

    def __init__(self, *args, **kwargs):
        self.profile = kwargs['initial']['profile']
        super(ChildForm, self).__init__(*args, **kwargs)

        if self.profile is not None:
            self.fields['city'].initial = self.profile.city
            self.fields['zip_code'].initial = self.profile.zip_code
            self.fields['house_number'].initial = self.profile.house_number
            self.fields['street'].initial = self.profile.street
            self.fields['insurance_company'].initial = self.profile.insurance_company
