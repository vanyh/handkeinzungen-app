from django.conf.urls import url
from .dal_views import SpeakerAltNameAC, QuoteBookSourceAC, QuoteQuoteTypeAC
from .models import Speaker, Book
from vocabs.models import SkosConcept


urlpatterns = [
    url(
        r'^speakeraltname-autocomplete/$', SpeakerAltNameAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='speakeraltname-autocomplete',
    ),
    url(
        r'^quotebooksource-autocomplete/$', QuoteBookSourceAC.as_view(
            model=Book, create_field='title',),
        name='quotebooksource-autocomplete',
    ),
    url(
        r'^quotequotetype-autocomplete/$', QuoteQuoteTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='quotequotetype-autocomplete',
    ),
    ]
