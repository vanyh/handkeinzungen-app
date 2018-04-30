from dal import autocomplete
from .models import Place, AlternativeName
from vocabs.models import SkosConcept, SkosConceptScheme
from . import dal_views


class PlaceAlternativeNameAC(autocomplete.Select2QuerySetView):

        def get_queryset(self):
            qs = AlternativeName.objects.all()

            if self.q:
                qs = qs.filter(name__icontains=self.q)

            return qs


class PlacePartOfAC(autocomplete.Select2QuerySetView):

        def get_queryset(self):
            qs = Place.objects.all()

            if self.q:
                qs = qs.filter(name__icontains=self.q)

            return qs
