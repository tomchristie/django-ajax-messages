from ajaxmessages import add_message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

INITIAL_MESSAGE = 'Your upload is being processed...'


@login_required
def index(request):
    if request.method == 'POST':
        add_message(request.user, INITIAL_MESSAGE)

    return render(request, 'index.html')
