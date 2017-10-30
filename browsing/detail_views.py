from django.views.generic.detail import DetailView
from bib.models import Work, Person, Quote, PartOfQuote
from words.models import GermanLemma, ForeignLemma


class GermanLemmaDetailView(DetailView):
    model = GermanLemma
    template_name = 'browsing/germanlemma_detail.html'


class ForeignLemmaDetailView(DetailView):
    model = ForeignLemma
    template_name = 'browsing/foreignlemma_detail.html'


class WorkDetailView(DetailView):
    model = Work
    template_name = 'browsing/work_detail.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'browsing/person_detail.html'


class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'browsing/quote_detail.html'


class PartOfQuoteDetailView(DetailView):
    model = PartOfQuote
    template_name = 'browsing/partofquote_detail.html'
