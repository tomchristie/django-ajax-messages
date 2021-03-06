from ajaxmessages.models import Message


def ajaxmessages(request):
    if not request.user.is_authenticated():
        return {}

    messages = Message.objects.filter(user=request.user).exclude(displayed=True)
    refresh = any([message.requires_refresh for message in messages])
    return {
        'ajaxmessages': messages,
        'ajaxmessages_refresh': refresh
    }
