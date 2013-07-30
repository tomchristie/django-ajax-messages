# Django AJAX Messages

**Auto-updating messages for Django.**

**Author:** Tom Christie, [Follow me on Twitter][twitter].

The `django-ajax-messages` package allows you to add auto-refreshing messages to your Django project.

## Installation

Install using pip:

    pip install django-ajax-messages

Add the following to your settings:

    INSTALLED_APPS = (
        ...
        'ajaxmessages',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'ajaxmessages.context_processors.ajaxmessages',
    )

## Adding messages to your templates

To include messages, add the following to any base template that
you want to display auto updating messages inside:

    {% include "ajaxmessages/messages.html" %}

There are also a number of javascript and stylesheet requirements that you'll want to include in you base template.  The only strict external requirement is jQuery, but you'll probably also want to include Bootstrap and FontAwesome to use the default style. 

#### Javascript requirements

You'll need to download and include jQuery, and include in the `ajaxmessages.js` static file that's included in this package.

If you're using the default template style, and want to allow users to dismiss alerts, you'll also want to include javascript for Bootstrap.

Place the following in your base template, just before the closing `</body>` tag.

    <script src="{% static 'js/jquery.js' %}"></script>
    <script src="{% static 'js/ajaxmessages.js' %}"></script>
    <script src="{% static 'js/bootstrap.js' %}"></script>

Download jQuery and Bootstrap and place the javascript files in your project's top level `static` folder:

     /static/js/bootstrap.js
     /static/js/jquery.js

#### Stylesheet requirements

If you're using the default template style, you'll want to include the Bootstrap CSS, as well as the fonts and styles for FontAwesome, that include the spinner icon used by the default style.

    <link href="{% static 'css/bootstrap.css' %}" rel="stylesheet" media="screen">
    <link href="{% static 'css/font-awesome.css' %}" rel="stylesheet">

Download Bootstrap and FontAwesome and place the stylesheets and fonts in your project's top level `static` folder:

    /static/css/bootstrap.js
    /static/css/font-awesome.css
    /static/font/FontAwesome.otf
    /static/font/fontawesome-webfont.eot
    /static/font/fontawesome-webfont.svg
    /static/font/fontawesome-webfont.ttf
    /static/font/fontawesome-webfont.woff

## License

Copyright © Tom Christie, DabApps.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[twitter]: http://twitter.com/_tomchristie
