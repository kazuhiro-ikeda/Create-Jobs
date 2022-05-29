from django import forms
from django.forms import ModelForm
from .models import JobModel


class DateInput(forms.DateInput):
    input_type = 'date'


class JobModelForm(ModelForm):

    class Meta:
        model = JobModel
        fields = ['title', 'date']
        widgets = {
            'date': DateInput(),
        }