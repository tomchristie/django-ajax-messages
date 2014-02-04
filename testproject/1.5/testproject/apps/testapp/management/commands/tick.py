from ajaxmessages.models import Message
from django.core.management.base import BaseCommand
from testproject.apps.testapp.views import INITIAL_MESSAGE
import ajaxmessages
import random
import time


class Command(BaseCommand):
    help = 'Update messages'

    def handle(self, *args, **options):
        while True:
            time.sleep(6)
            queryset = Message.objects.filter(status=ajaxmessages.PENDING)
            for message in queryset:
                if message.text == INITIAL_MESSAGE:
                    message.text = 'Scaling and cropping...'
                else:
                    if random.choice([True, False]):
                        message.text = 'Upload success'
                        message.status = ajaxmessages.SUCCESS
                    else:
                        message.text = 'Upload failed'
                        message.status = ajaxmessages.FAILURE
                message.save()
