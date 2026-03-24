from django import template
register=template.Library()

@register.filter
def vowels(value):
    res=''
    for ch in value:
        if ch in "AEIOUaeiou":
            res+=ch
    return res