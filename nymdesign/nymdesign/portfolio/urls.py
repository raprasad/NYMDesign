from django.conf.urls import patterns, include, url

urlpatterns = patterns('nymdesign.portfolio.views',

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^view/(?P<portfolio_slug>\w([\w|\.\-])*)/$', 'view_single_project', name='view_single_project'),

     url(r'^view/(?P<portfolio_slug>\w([\w|\.\-])*)/(?P<image_number>\d{1,3})/$', 'view_single_project', name='view_single_project_with_image_num'),

     url(r'^media/(?P<media_type_slug>\w([\w|\.\-])*)/$', 'view_media_category', name='view_media_category'),

     url(r'^$', 'view_homepage', name='view_homepage'),
  
)
