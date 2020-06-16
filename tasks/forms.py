from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User


class CampFilter(forms.Form):
    age = forms.IntegerField(required=False, label="Věk:")
    leader = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Hlavní vedoucí:")
    # TODO: Filter only leaders
