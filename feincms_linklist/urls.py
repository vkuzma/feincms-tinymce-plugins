""" Add this url path to your patterns:

    url(r'', include('feincms_linklist.urls')),

"""

from django.conf.urls import *

urlpatterns = patterns('feincms_linklist.views',
    url(r'^linklist.js$', 'linklist', name='feincms_linklist_links'),
)
