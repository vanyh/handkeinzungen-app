from django.views.generic.detail import DetailView
from bib.models import Work


class WorkDetailView(DetailView):
    model = Work
    template_name = 'browsing/work_detail.html'
