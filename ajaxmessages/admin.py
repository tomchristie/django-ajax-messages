from ajaxmessages.models import Message
from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'text', 'displayed')


admin.site.register(Message, MessageAdmin)
