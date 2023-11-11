from django import forms
from user_profile.models import UserProfile
from mysite.constants import COUNTRY_ID_CHOICE

GENDER_CHOICE = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
]

AGE_CHOICE = [tuple([year, year]) for year in range(1, 80)]


class UserProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICE)
    age = forms.ChoiceField(required=True, choices=AGE_CHOICE)
    country = forms.ChoiceField(required=True, choices=COUNTRY_ID_CHOICE)

    class Meta:
        model = UserProfile
        fields = ("gender", "age", "country")
