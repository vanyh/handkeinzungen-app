from dal import autocomplete
from .models import Speaker, Quote, Book, Work, PartOfQuote, Speaker
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


class QuotePartOfQuoteAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Quote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class QuoteSelfTranslationAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Quote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class PartOfQuotePartOfQuoteAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Quote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class PartOfQuoteSourceAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Work.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs


class PartOfQuoteFollowsAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = PartOfQuote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class PartOfQuoteTranslationAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = PartOfQuote.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs


class PartOfQuoteLanguageAC(autocomplete.Select2QuerySetView):

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


class PartOfQuotePartOfQuoteTypeAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='TypeofText'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PartOfQuoteSpeakerAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Speaker.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
