from django import template
from django.conf import settings
from django.contrib import staticfiles

register = template.Library()

@register.filter(name='bscss')
def bootstrap_css(f=settings.BOOTSTRAP_THEME):
    print f
    if f:
        return ''.join((settings.BOOTSTRAP_THEME, '-bootstrap.min.css'))
    else:
        return 'bootstrap.min.css'