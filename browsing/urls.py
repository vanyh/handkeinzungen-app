from django.conf.urls import url
from . import detail_views
from . import views

urlpatterns = [
    url(r'partofquotes/$', views.PartOfQuoteListView.as_view(), name='browse_partofquotes'),
    url(r'^partofquote/(?P<pk>[0-9]+)$', detail_views.PartOfQuoteDetailView.as_view(),
        name='partofquote_detail'),
    url(r'works/$', views.WorkListView.as_view(), name='browse_works'),
    url(r'^work/(?P<pk>[0-9]+)$', detail_views.WorkDetailView.as_view(),
        name='work_detail'),
    url(r'persons/$', views.PersonListView.as_view(), name='browse_persons'),
    url(r'^person/(?P<pk>[0-9]+)$', detail_views.PersonDetailView.as_view(),
        name='person_detail'),
    url(r'quotes/$', views.QuoteListView.as_view(), name='browse_quotes'),
    url(r'^quote/(?P<pk>[0-9]+)$', detail_views.QuoteDetailView.as_view(),
        name='quote_detail'),
    url(r'foreignlemmas/$', views.ForeignLemmaListView.as_view(), name='browse_foreignlemmas'),
    url(r'^foreignlemma/(?P<pk>[0-9]+)$', detail_views.ForeignLemmaDetailView.as_view(),
        name='foreignlemma_detail'),
    url(r'germanlemmas/$', views.GermanLemmaListView.as_view(), name='browse_germanlemmas'),
    url(r'^germanlemma/(?P<pk>[0-9]+)$', detail_views.GermanLemmaDetailView.as_view(),
        name='germanlemma_detail'),
    url(r'books/$', views.BookListView.as_view(), name='browse_books'),
    url(r'^book/(?P<pk>[\w\-]+)$', detail_views.BookDetailView.as_view(),
        name='book_detail'),
    url(r'places/$', views.PlaceListView.as_view(), name='browse_places'),
    url(r'^places/(?P<pk>[0-9]+)$', detail_views.PlaceDetailView.as_view(),
        name='place_detail'),
    url(r'altnames/$', views.AlternativeNameListView.as_view(), name='browse_altnames'),
    url(r'^altnames/(?P<pk>[0-9]+)$', detail_views.AlternativeNameDetailView.as_view(),
        name='alternativename_detail'),
    url(r'speakers/$', views.SpeakerListView.as_view(), name='browse_speakers'),
    url(r'^speakers/(?P<pk>[0-9]+)$', detail_views.SpeakerDetailView.as_view(),
        name='speaker_detail')
]
