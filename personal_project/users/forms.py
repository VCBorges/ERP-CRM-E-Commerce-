from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm



class CreateUserForm(SignupForm):

    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    document = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    street = forms.CharField(required=False)
    number = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    birthday = forms.DateField(required=False)
    gender = forms.CharField(required=False)
    
    
    def save(self, request):
        user = super().save(request)
        user.middle_name = self.cleaned_data.get('middle_name')
        user.document = self.cleaned_data.get('document')
        user.phone = self.cleaned_data.get('phone')
        user.street = self.cleaned_data.get('street')
        user.number = self.cleaned_data.get('number')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.country = self.cleaned_data.get('country')
        user.gender = self.cleaned_data.get('gender')
        user.birthday = self.cleaned_data.get('birthday')
        user.save()
        return user