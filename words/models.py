from django.db import models
from idprovider.models import IdProvider
from bib.models import Quote
from vocabs.models import SkosConcept


class GermanLemma(IdProvider):
    lemma = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    pos = models.ForeignKey(SkosConcept, blank=True, null=True)
    language = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name='language_of_german_lemma',
    )

    def save(self, *args, **kwargs):
        deu, _ = SkosConcept.objects.get_or_create(
            pref_label='Deutsch'
        )
        self.language = deu
        super(GermanLemma, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.lemma)


class ForeignLemma(IdProvider):
    lemma = models.CharField(max_length=250, blank=True, null=True)
    pos = models.ForeignKey(SkosConcept, blank=True, null=True)
    german = models.ManyToManyField(GermanLemma, blank=True)
    language = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='language_of_foreign_lemma'
    )
    used_in = models.ManyToManyField(Quote, blank=True)

    def __str__(self):
        return "{}".format(self.lemma)
