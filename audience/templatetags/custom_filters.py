from django import template

register = template.Library()
all_month = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")


@register.filter(name="sport_datetime")
def sport_datetime(value):
    date = value.split("T")[0].split("-")
    month = date[1]
    day = date[2]
    value = f"{day} {all_month[int(month) - 1]}"
    return value
