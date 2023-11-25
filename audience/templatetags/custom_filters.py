from django import template
from mysite.constants import COUNTRY_ID_CHOICE

register = template.Library()
all_month = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")


@register.filter(name="sport_datetime")
def sport_datetime(value):
    date = value.split("T")[0].split("-")
    month = date[1]
    day = date[2]
    value = f"{day} {all_month[int(month) - 1]}"
    return value

@register.filter
def split_string(value):
    return value.split(" ")

@register.filter(name='get_country_name')
def get_country_name(country_code):
    for code, name in COUNTRY_ID_CHOICE:
        if code == country_code:
            return code if len(name) > 15 else name
    return country_code  # Return the code if the name is not found
