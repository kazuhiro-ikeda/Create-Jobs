from django import forms
from django.forms import ModelForm
from .models import Jobs

class DateInput(forms.DateInput):
    input_type = 'date'


class TextAreaInput(forms.Textarea):
    input_type = 'textarea'

class JobsForm(ModelForm):
    """CHOICES1 = (
        ('株式会社タミアス', '株式会社タミアス'),
        ('株式会社らむだ', '株式会社らむだ'),
        ('合同会社マーリー', '合同会社マーリー')
    )
    company = forms.ChoiceField(choices=CHOICES1)
    """


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
            'country',
            'jobtype'
        ]

class JobsImportForm(forms.Form):
    file = forms.FileField(label='jobs.csv')