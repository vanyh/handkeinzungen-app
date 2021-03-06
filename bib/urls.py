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
        name='quote_delete'),
    url(r'^partofquote/edit/(?P<pk>[0-9]+)$', views.PartOfQuoteUpdate.as_view(),
        name='partofquote_edit'),
    url(r'^partofquote/create/$', views.PartOfQuoteCreate.as_view(),
        name='partofquote_create'),
    url(r'^partofquote/delete/(?P<pk>[0-9]+)$', views.PartOfQuoteDelete.as_view(),
        name='partofquote_delete'),
    url(r'^germanlemma/edit/(?P<pk>[0-9]+)$', views.GermanLemmaUpdate.as_view(),
        name='germanlemma_edit'),
    url(r'^germanlemma/create/$', views.GermanLemmaCreate.as_view(),
        name='germanlemma_create'),
    url(r'^germanlemma/delete/(?P<pk>[0-9]+)$', views.GermanLemmaDelete.as_view(),
        name='germanlemma_delete'),
    url(r'^foreignlemma/edit/(?P<pk>[0-9]+)$', views.ForeignLemmaUpdate.as_view(),
        name='foreignlemma_edit'),
    url(r'^foreignlemma/create/$', views.ForeignLemmaCreate.as_view(),
        name='foreignlemma_create'),
    url(r'^foreignlemma/delete/(?P<pk>[0-9]+)$', views.ForeignLemmaDelete.as_view(),
        name='foreignlemma_delete'),
    url(r'^book/edit/(?P<pk>[\w\-]+)$', views.BookUpdate.as_view(),
        name='book_edit'),
    url(r'^book/delete/(?P<pk>[\w\-]+)$', views.BookDelete.as_view(),
        name='book_delete'),
    url(r'^speaker/edit/(?P<pk>[0-9]+)$', views.SpeakerUpdate.as_view(),
        name='speaker_edit'),
    url(r'^speaker/delete/(?P<pk>[0-9]+)$', views.SpeakerDelete.as_view(),
        name='speaker_delete'),
    url(r'^speaker/create/$', views.SpeakerCreate.as_view(),
        name='speaker_create')
]
