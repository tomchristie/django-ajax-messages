from ajaxmessages.models import Message
from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
