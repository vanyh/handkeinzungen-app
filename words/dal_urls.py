from django.conf.urls import url
from .dal_views import ForeignLemmaGermanAC, ForeignLemmaPOSAC, ForeignLemmaLanguageAC, ForeignLemmaUsedInAC, GermanLemmaPOSAC, GermanLemmaLanguageAC
from .models import GermanLemma, ForeignLemma
from vocabs.models import SkosConcept


urlpatterns = [
    url(
        r'^foreignlemmagerman-autocomplete/$', ForeignLemmaGermanAC.as_view(
            model=GermanLemma, create_field='lemma',),
        name='foreignlemmagerman-autocomplete',
    ),
    url(
        r'^foreignlemmapos-autocomplete/$', ForeignLemmaPOSAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='foreignlemmapos-autocomplete',
    ),
    url(
        r'^foreignlemmalanguage-autocomplete/$', ForeignLemmaLanguageAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='foreignlemmalanguage-autocomplete',
    ),
    url(
        r'^foreignlemmausedin-autocomplete/$', ForeignLemmaUsedInAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='foreignlemmausedin-autocomplete',
    ),
    url(
        r'^germanlemmapos-autocomplete/$', GermanLemmaPOSAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='germanlemmapos-autocomplete',
    ),
    url(
        r'^germanlemmalanguage-autocomplete/$', GermanLemmaLanguageAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='germanlemmalanguage-autocomplete',
    ),
]
