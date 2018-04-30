from django.conf.urls import url
from .dal_views import PlaceAlternativeNameAC, PlacePartOfAC
from .models import Place, AlternativeName
from vocabs.models import SkosConcept


urlpatterns = [
    url(
        r'^placealternativename-autocomplete/$', PlaceAlternativeNameAC.as_view(
            model=AlternativeName, create_field='name',),
        name='placealternativename-autocomplete',
    ),
    url(
        r'^placepartof-autocomplete/$', PlacePartOfAC.as_view(
            model=Place, create_field='name',),
        name='placepartof-autocomplete',
    )
    ]
