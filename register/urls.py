from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<agency_id>[0-9]+)/$', views.agencydetails, name='agencydetails'),
    url(r'^sign-in/$', views.sign_in, name='sign-in'),
    url(r'^create/$', views.CreateContracts, name='createcontracts'),
]