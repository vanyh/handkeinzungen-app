# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^synczotero/$', views.sync_zotero, name="synczotero"),
    url(r'^synczotero/result$', views.sync_zotero_action, name="synczotero_action"),
    url(r'^person/edit/(?P<pk>[0-9]+)$', views.PersonUpdate.as_view(),
        name='person_edit'),
    url(r'^person/create/$', views.PersonCreate.as_view(),
        name='person_create'),
    url(r'^person/delete/(?P<pk>[0-9]+)$', views.PersonDelete.as_view(),
        name='person_delete'),
    url(r'^work/edit/(?P<pk>[0-9]+)$', views.WorkUpdate.as_view(),
        name='work_edit'),
    url(r'^work/create/$', views.WorkCreate.as_view(),
        name='work_create'),
    url(r'^work/delete/(?P<pk>[0-9]+)$', views.WorkDelete.as_view(),
        name='work_delete'),
    url(r'^quote/edit/(?P<pk>[0-9]+)$', views.QuoteUpdate.as_view(),
        name='quote_edit'),
    url(r'^quote/create/$', views.QuoteCreate.as_view(),
        name='quote_create'),
    url(r'^quote/delete/(?P<pk>[0-9]+)$', views.QuoteDelete.as_view(),
        name='quote_delete')
]
