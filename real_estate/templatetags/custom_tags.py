from django import template
from real_estate.models import RealEstate


register = template.Library()

@register.filter
def format_price(value):
    return f'{value:,}'.replace(',', ' ')


@register.simple_tag
def property_count():
    return RealEstate.objects.count()
