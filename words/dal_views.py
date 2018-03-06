from dal import autocomplete
from .models import GermanLemma


class GermanLemmaAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = GermanLemma.objects.all()

        if self.q:
            qs = qs.filter(lemma__icontains=self.q)

        return qs
