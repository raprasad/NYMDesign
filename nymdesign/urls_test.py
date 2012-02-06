from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^nymdesign/', include('nymdesign.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^portfolio/', include('nymdesign.portfolio.urls')),

    (r'^info/', include('nymdesign.info_pages.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin-page/(.*)', admin.site.root),

     (r'^', include('nymdesign.portfolio.urls')),

)

