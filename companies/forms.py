from django import forms
from companies.models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'location',
            'number_of_trucks',
            'logo',
        ]