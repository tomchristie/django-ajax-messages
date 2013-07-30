from ajaxmessages.models import Message
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.views.generic import View


class MessagesView(View):
    template_name = 'ajaxmessages/messages.html'

    def get_messages(self, request):
        messages = Message.objects.filter(user=request.user)
        filter_ids = request.GET.get('filter', '').split(',')
        if filter_ids:
            messages = messages.filter(id__in=filter_ids)
        return messages

    def get(self, request):
        if not request.user.is_authenticated():
            raise PermissionDenied()

        # Note that we return a regular Context, not a RequestContext,
        # as we don't want the `ajaxmessages` content processor kicking in.
        context = {'ajaxmessages': self.get_messages(request)}

        return render_to_response(self.template_name, context)


messages = MessagesView.as_view()
