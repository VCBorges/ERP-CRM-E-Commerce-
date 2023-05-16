from django import forms

from companys.models import Company


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'website',
            'document',
            'industry',
            'size',
        ]
        