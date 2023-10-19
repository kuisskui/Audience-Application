from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

GENDER_CHOICE = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
]

AGE_CHOICE = [tuple([year, year]) for year in range(1, 80)]

COUNTRY_ID_CHOICE = [
    ("US", "United State"),
    ("TH", "Thailand")
]

# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField(required=True, widget=forms.Select(choices=GENDER_CHOICE, attrs={'class': 'custom-select-gender'}))
    age = forms.CharField(required=True, widget=forms.Select(choices=AGE_CHOICE, attrs={'class': 'custom-select-age'}))
    country = forms.CharField(required=True, widget=forms.Select(choices=COUNTRY_ID_CHOICE, attrs={'class': 'custom-select-country'}))

    class Meta:
        model = User
        fields = ("username", "age", "gender", "country", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
