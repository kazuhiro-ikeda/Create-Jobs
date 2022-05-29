from django import forms
from django.forms import ModelForm
from .models import Jobs

class DateInput(forms.DateInput):
    input_type = 'date'


class TextAreaInput(forms.Textarea):
    input_type = 'textarea'

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        widgets = [

        ]
        fields = [
            'title',
            'company'
        ]

class JobsImportForm(forms.Form):
    file = forms.FileField(label='jobs.csv')