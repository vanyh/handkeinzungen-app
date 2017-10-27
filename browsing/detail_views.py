from django.views.generic.detail import DetailView
from bib.models import Work, Person, Quote


class WorkDetailView(DetailView):
    model = Work
    template_name = 'browsing/work_detail.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'browsing/person_detail.html'


class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'browsing/quote_detail.html'
