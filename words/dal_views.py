from dal import autocomplete
from .models import GermanLemma, ForeignLemma, Quote
from vocabs.models import SkosConcept, SkosConceptScheme
from . import dal_views


class ForeignLemmaGermanAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = GermanLemma.objects.all()

        if self.q:
            qs = qs.filter(lemma__icontains=self.q)

        return qs


class ForeignLemmaPOSAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='POS'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class ForeignLemmaLanguageAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='Sprachen'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class ForeignLemmaUsedInAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Quote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class GermanLemmaPOSAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='POS'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class GermanLemmaLanguageAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='Sprachen'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs
