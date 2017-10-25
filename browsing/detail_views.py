from django.views.generic.detail import DetailView
from bib.models import Work, Person


class WorkDetailView(DetailView):
    model = Work
    template_name = 'browsing/work_detail.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'browsing/person_detail.html'
