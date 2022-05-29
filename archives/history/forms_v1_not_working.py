from django import forms
from .models import JobModel


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class DateInput(forms.DateInput):
    input_type = 'date'


class TextAreaInput(forms.Textarea):
    input_type = 'textarea'


class JobModelForm(forms.Form):
    title = forms.CharField(max_length=256)
    date = forms.DateTimeField()
    company = forms.CharField(max_length=256, initial='合同会社マーリー')
    country = forms.CharField(max_length=10, initial='日本')
    postalcode = forms.CharField(max_length=10, initial='448-0007')
    state = forms.CharField(max_length=10, initial='愛知県')
    city = forms.CharField(max_length=10, initial='刈谷市')
    rawlocation = forms.CharField(max_length=256, required=False)
    streetaddress = forms.CharField(max_length=256, required=False)
    email = forms.EmailField(max_length=256, required=False)
    station = forms.CharField(widget=TextAreaInput, required=False)
    subwayaccess = forms.CharField(widget=TextAreaInput, required=False)
    category = forms.CharField(max_length=256, required=False)
    jobtype = forms.CharField(max_length=256, required=False)
    description = forms.CharField(widget=TextAreaInput, initial='<h2>仕事内容</h2>')
    salary = forms.CharField(widget=TextAreaInput, initial='350,000円 / 月')
    rawsalary = forms.CharField(widget=TextAreaInput, required=False)
    timeshift = forms.CharField(widget=TextAreaInput, required=False)
    education = forms.CharField(widget=TextAreaInput, required=False)
    experience = forms.CharField(widget=TextAreaInput, required=False)
    benefits = forms.CharField(widget=TextAreaInput, required=False)
    expirationdate = forms.DateField(required=False)
    expdate = forms.DateField(required=False)
    tracking_url = forms.CharField(max_length=256, required=False)
    imageUrls = forms.CharField(max_length=500, required=False)
    hires = forms.CharField(max_length=256, required=False)
    keywords = forms.CharField(max_length=256, required=False)

    class Meta:
        model = JobModel

        fields = [
            'title',
            'date',
            'company',
            'country',
            'postalcode',
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

        #exclude = ('id', 'created_at', 'upadted_at',)
