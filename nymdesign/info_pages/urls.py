from django.conf.urls import include, url
from nymdesign.info_pages import views

urlpatterns = [

     url(r'^about/$',
         views.view_about,
         name='view_about'),

     url(r'^contact/$',
         views.view_contact,
         name='view_contact'),

     url(r'^clients/$',
         views.view_clients,
         name='view_clients'),

]
