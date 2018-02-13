from django.views.generic.detail import DetailView
from bib.models import Work, Person, Quote, PartOfQuote, Book, Speaker
from words.models import GermanLemma, ForeignLemma
from places.models import Place, AlternativeName


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


class BookDetailView(DetailView):
    model = Book
    template_name = 'browsing/book_detail.html'


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'


class AlternativeNameDetailView(DetailView):
        model = AlternativeName
        template_name = 'places/alternativenames_detail.html'


class SpeakerDetailView(DetailView):
        model = Speaker
        template_name = 'browsing/speaker_detail.html'
