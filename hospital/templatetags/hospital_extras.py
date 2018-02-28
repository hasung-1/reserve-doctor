from django import template
import random 

register = template.Library()

#랜덤으로 숫자를 뽑는 함수
@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)