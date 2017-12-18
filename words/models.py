from django.db import models
from django.core.urlresolvers import reverse
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

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_germanlemmas')

    def get_next(self):
        next = GermanLemma.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = GermanLemma.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def save(self, *args, **kwargs):
        deu, _ = SkosConcept.objects.get_or_create(
            pref_label='Deutsch'
        )
        self.language = deu
        super(GermanLemma, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('browsing:germanlemma_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}".format(self.lemma)

    @classmethod
    def get_alternative_classname(self):
        """Returns the alternative name of the class.
        Needed to present the human readable name of class"""
        return 'Deutsche Lemmata'


class ForeignLemma(IdProvider):
    lemma = models.CharField(max_length=250, blank=True, null=True)
    pos = models.ForeignKey(SkosConcept, blank=True, null=True)
    german = models.ManyToManyField(GermanLemma, blank=True, related_name="has_translation")
    language = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='language_of_foreign_lemma'
    )
    used_in = models.ManyToManyField(Quote, blank=True, related_name="has_lemma")

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_foreignlemmas')

    def get_next(self):
        next = ForeignLemma.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = ForeignLemma.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('browsing:foreignlemma_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}".format(self.lemma)

    @classmethod
    def get_alternative_classname(self):
        """Returns the alternative name of the class.
        Needed to present the human readable name of class"""
        return 'Fremdsprachige Lemmata'
