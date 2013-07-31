from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

STATUS_CHOICES = (
    ('p', 'Pending'),
    ('s', 'Success'),
    ('f', 'Failure'),
)


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    text = models.CharField(max_length=1000)
    displayed = models.BooleanField(default=False)

    tag_map = {
        'p': 'alert-info',
        's': 'alert-success',
        'f': 'alert-danger',
    }

    icon_map = {
        'p': '<i class="icon-spinner icon-spin icon-large"></i>',
        's': '',
        'f': ''
    }

    refresh_map = {
        'p': True,
        's': False,
        'f': False
    }

    allow_dismiss_map = {
        'p': False,
        's': True,
        'f': True
    }

    @property
    def tag(self):
        return self.tag_map[self.status]

    @property
    def icon(self):
        return mark_safe(self.icon_map[self.status])

    @property
    def requires_refresh(self):
        return self.refresh_map[self.status]

    @property
    def allow_dismiss(self):
        return self.allow_dismiss_map[self.status]

    def mark_as_displayed(self):
        if self.status != 'p':
            self.displayed = True
            self.save()

    def __str__(self):
        return self.text
