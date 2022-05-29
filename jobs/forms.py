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
        widgets = {
            'publish': DateInput,
            'validthrough': DateInput
        }
        fields = [
            'title',
            'publish',
            'validthrough',
            'company',
            'country'
        ]

class JobsImportForm(forms.Form):
    file = forms.FileField(label='jobs.csv')