from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testproject.apps.testapp.views.index'),
    url(r'^messages/$', 'ajaxmessages.views.messages', name='ajaxmessages'),
    url(r'^admin/', include(admin.site.urls)),
)
