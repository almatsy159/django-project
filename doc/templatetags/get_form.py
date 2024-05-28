from django import template as tpl

register = tpl.Library()
print(f"loaded python : {__name__}")