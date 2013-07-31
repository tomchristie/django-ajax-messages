from ajaxmessages.models import Message
from testproject.apps.testapp.views import INITIAL_MESSAGE
import ajaxmessages
import random


class UpdateExampleMessagesMiddleware(object):
    def process_request(self, request):
        queryset = Message.objects.filter(
            status=ajaxmessages.PENDING
        ).exclude(
            displayed=True
        )

        for message in queryset:
            if message.message == INITIAL_MESSAGE:
                message.message = '...Scaling and cropping...'
            else:
                if random.choice([True, False]):
                    message.message = 'Upload success'
                    message.status = ajaxmessages.SUCCESS
                else:
                    message.message = 'Upload failed'
                    message.status = ajaxmessages.FAILURE
            message.save()
