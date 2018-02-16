from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from places.apis_views import PlaceViewSet, GeoJsonViewSet
from words.api_views import *
from bib.api_views import *


from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'geojson', GeoJsonViewSet, base_name='places')
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'Book', BookViewSet)
router.register(r'work', WorkViewSet)
router.register(r'person', PersonViewSet)
router.register(r'speaker', SpeakerViewSet)
router.register(r'quote', QuoteViewSet)
router.register(r'partofquote', PartOfQuoteViewSet)
router.register(r'germanlemma', GermanLemmaViewSet)
router.register(r'foreignlemma', ForeignLemmaViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^sparql/', include('sparql.urls', namespace='sparql')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'^bib/', include('bib.urls', namespace='bib')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^words-ac/', include('words.dal_urls', namespace='words-ac')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]
