from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import COUNTRY_ID_CHOICE

GENDER_CHOICE = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
]

AGE_CHOICE = [tuple([year, year]) for year in range(1, 80)]


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICE)
    age = forms.ChoiceField(required=True, choices=AGE_CHOICE)
    country = forms.ChoiceField(required=True, choices=COUNTRY_ID_CHOICE)

    class Meta:
        model = User
        fields = ("username", "age", "gender", "country", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
