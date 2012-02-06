from django.conf.urls.defaults import *

urlpatterns = patterns('nymdesign.info_pages.views',

     url(r'^about/$', 'view_about', name='view_about'),

     url(r'^contact/$', 'view_contact', name='view_contact'),

     url(r'^clients/$', 'view_clients', name='view_clients'),

)
