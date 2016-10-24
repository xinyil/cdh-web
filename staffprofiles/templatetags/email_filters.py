from django import template

register = template.Library()


@register.filter(name='atdot')
def atdot(string):

    string = string.replace('@','(at)').replace('.','(dot)')

    return string
