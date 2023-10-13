from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

GENDER_CHOICE = [
    ("male", "Male"),
    ("female", "Female")
]

YEAR_CHOICE = [tuple([year, year]) for year in range(datetime.now().year, datetime.now().year - 80, -1)]

COUNTRY_ID_CHOICE = [
    ("US", "United State"),
    ("TH", "Thailand")
]


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField(required=True, widget=forms.Select(choices=GENDER_CHOICE))
    year = forms.CharField(required=True, widget=forms.Select(choices=YEAR_CHOICE))
    country_id = forms.CharField(required=True, widget=forms.Select(choices=COUNTRY_ID_CHOICE))

    class Meta:
        model = User
        fields = ("username", "year", "gender", "country_id", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
