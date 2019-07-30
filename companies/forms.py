from django import forms
from companies.models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'logo',
            'location',
            'number_of_trucks'
        ]