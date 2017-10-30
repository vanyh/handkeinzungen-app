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
]
