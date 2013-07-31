from django import template

register = template.Library()


def mark_as_displayed(messages):
    for message in messages:
        message.mark_as_displayed()
    return ''

register.simple_tag(mark_as_displayed)
