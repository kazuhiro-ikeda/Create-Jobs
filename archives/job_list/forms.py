from django import forms
from django.forms import ModelForm, ChoiceField
from .models import JobModel


class DateInput(forms.DateInput):
    input_type = 'date'


class TextAreaInput(forms.Textarea):
    input_type = 'textarea'


class JobModelForm(ModelForm):

    class Meta:
        model = JobModel
        widgets = {
            'publish': DateInput(),
            'validthrough': DateInput(),
            'description': TextAreaInput(),
        }
        fields = [
            'title',
            'publish',
            'validthrough',
            'company',
            'country'
        ]


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='jobs.csv')


