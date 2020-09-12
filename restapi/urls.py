from django.conf.urls import url
from restapi import views

urlpatterns = [
    url(r'^api/leads$', views.leads_post),
    url(r'^api/leads/(?P<pk>[0-9]+)$', views.leads_detail),
    url(r'^api/mark_lead/(?P<pk>[0-9]+)$', views.mark_lead)
]