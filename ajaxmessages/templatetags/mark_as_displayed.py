from django import template

register = template.Library()


def mark_as_displayed(messages):
    for message in messages:
        if message.status != 'p':
            message.displayed = True
            message.save()
    return ''

register.simple_tag(mark_as_displayed)
