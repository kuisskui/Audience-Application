from django import template
from mysite.constants import COUNTRY_ID_CHOICE

register = template.Library()

@register.filter(name='get_country_name')
def get_country_name(country_code):
    for code, name in COUNTRY_ID_CHOICE:
        if code == country_code:
            return name
    return country_code  # Return the code if the name is not found