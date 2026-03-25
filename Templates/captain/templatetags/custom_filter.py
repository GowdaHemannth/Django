from django import template
register=template.Library()

@register.filter
def vowels(Hammmmmmmm):
    res=''
    for ch in Hammmmmmmm:
        if ch not in "AEIOUaeiou":
            res+=ch
    return res

@register.filter
def Divisible(value,Number):
    if(value%Number==0):
        return '{ Divisble}'
    else:
        return False
 
@register.filter
def Add(value,Number):
    return value+Number    

@register.filter
def Replace(value,args):
    Character,NewCharacter=args.split(',')
    res=''
    for i in range(0,len(value)):
        if value[i]==Character:
            res=res+NewCharacter
        else:
            res=res+value[i]
            
@register.filter
def even(value):
    if value%2==0:
        return '{Yes it is EVEN}'
  
              