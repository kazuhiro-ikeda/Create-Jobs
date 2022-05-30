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
            'date': DateInput(),
            'expirationdate': DateInput(),
            'expdate': DateInput(),
            'station': TextAreaInput(),
            'subwayaccess': TextAreaInput(),
            'description': TextAreaInput(),
            'rawsalary': TextAreaInput(),
            'timeshift': TextAreaInput(),
            'education': TextAreaInput(),
            'experience': TextAreaInput(),
            'benefits': TextAreaInput(),
        }
        fields = [
            'title',
            'publish',
            'validthrough',
            'company',
            'country',
            'state',
            'city',
            'rawlocation',
            'streetaddress',
            'email',
            'station',
            'subwayaccess',
            'category',
            'jobtype',
            'description',
            'salary',
            'rawsalary',
            'timeshift',
            'education',
            'experience',
            'benefits',
            'expirationdate',
            'expdate',
            'tracking_url',
            'imageUrls',
            'hires',
            'keywords'
        ]


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='jobs.csv')


