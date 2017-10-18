from django.db import models
from django.conf import settings
from idprovider.models import IdProvider
from vocabs.models import SkosConcept
from places.models import Place


class Book(IdProvider):
    zoterokey = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    publication_title = models.CharField(max_length=100, blank=True, null=True)
    short_title = models.CharField(max_length=500, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    pub_place = models.ManyToManyField(Place, blank=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    issn = models.CharField(max_length=100, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    book_type = models.ManyToManyField(SkosConcept, blank=True)

    def get_zotero_url(self):
        "Returns the objects URL pointing to its Zotero entry"
        try:
            return "/".join([settings.Z_BASE_URL, settings.Z_COLLECTION, 'itemKey', self.zoterokey])
        except:
            return None

    def __str__(self):
        return "{}, {}".format(self.author, self.title)


class TextChunk(IdProvider):
    """Provides the context of quotes"""
    book_source = models.ForeignKey(Book, blank=True, null=True)
    startpage = models.IntegerField(blank=True)
    endpage = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    chunk_type = models.ManyToManyField(SkosConcept, blank=True)

    def __str__(self):
        return "{}".format(self.text)


class Quote(IdProvider):
    """A class modeling quotes"""
    text = models.CharField(blank=True, max_length=500)
    part_of = models.ManyToManyField(TextChunk, blank=True)
    source = models.ForeignKey(Book, blank=True, null=True)
    follows = models.ManyToManyField('self', blank=True, related_name='has_follower')
    translates = models.ManyToManyField('self', blank=True, related_name='has_translation')
    language = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='quote_language')
    quote_type = models.ManyToManyField(SkosConcept, blank=True, related_name='quote_type')

    def __str__(self):
        return "{}".format(self.text)
