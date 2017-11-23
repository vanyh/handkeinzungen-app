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
        name='person_delete')
]
