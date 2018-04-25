from dal import autocomplete
from .models import Speaker, Quote, Book
from vocabs.models import SkosConcept, SkosConceptScheme
from . import dal_views


class SpeakerAltNameAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='speaker_altname'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class QuoteBookSourceAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Book.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs


class QuoteQuoteTypeAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='TypeofWork'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs
