from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Candidate, ContactForCandidate, AddressForCandidate
# from django.core.exceptions import NON_FIELD_ERRORS


class UserForm(UserCreationForm):
  class Meta:
    model = User
    widgets = {
               "email": forms.TextInput(attrs={'class': "form-control", 'type': "email"}),
               "first_name": forms.TextInput(attrs={'class': "form-control", 'required': "required"}),
               "last_name": forms.TextInput(attrs={'class': "form-control", 'required': "required"}),
               }
    fields = ['last_name', 'email', 'first_name',]


class CandidateForm(ModelForm):



  class Meta:
    model = Candidate
    widgets = {
                "dob": forms.DateInput(attrs={'class': "form-control",}),
                "gender": forms.Select(attrs={'class': "form-control", "data-toggle": "select"}),
                "designation": forms.TextInput(attrs={'class': "form-control", 'required': "required",}),
                "reports_to": forms.TextInput(attrs={'class': "form-control", 'required': "required",}),
                "annual_salary": forms.NumberInput(attrs={'class': "form-control", 'required': "required",}),
                "issue_date": forms.DateInput(attrs={'class': "form-control",}),
                "joining_date": forms.DateInput(attrs={'class': "form-control",}),

               }
    exclude = ('user',)

 


class AddressForCandidateForm(ModelForm):
  class Meta:
    model = AddressForCandidate

    widgets = {"addressline1": forms.TextInput(attrs={'class': "form-control", }),
               "addressline2": forms.TextInput(attrs={'class': "form-control"}),
               "area": forms.TextInput(attrs={'class': "form-control", }),
               "zipcode": forms.NumberInput(attrs={'class': "form-control", }),
               "city": forms.Select(attrs={'class': "chained form-control", }),
               "state": forms.Select(attrs={'class': "chained form-control", }),
               "country": forms.Select(attrs={'class': "chained form-control",}),
               "landmark": forms.TextInput(attrs={'class': "form-control", }),

               }
    exclude = ('candidate',)


class ContactForCandidateForm(ModelForm):
  class Meta:
    model = ContactForCandidate

    widgets = {"phone": forms.NumberInput(attrs={'class': "form-control", 'required': "required"}),
               "alternate_phone": forms.NumberInput(attrs={'class': "form-control", }),
               }
    fields = ['phone', 'alternate_phone']


