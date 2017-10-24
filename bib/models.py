from django.db import models
from django.conf import settings
from idprovider.models import IdProvider
from vocabs.models import SkosConcept
from places.models import Place


class Person(IdProvider):
    """Eine Person, zum Beispiel die Verfasserin eines Werks."""
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    person_gnd = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Book(models.Model):
    zoterokey = models.CharField(primary_key=True, max_length=100, blank=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="Author Name fetched from Zotero"
    )
    book_author = models.ManyToManyField(Person, blank=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    publication_title = models.CharField(max_length=100, blank=True, null=True)
    short_title = models.CharField(max_length=500, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    pub_place = models.ManyToManyField(Place, blank=True)
    isbn = models.CharField(max_length=500, blank=True, null=True)
    issn = models.CharField(max_length=500, blank=True, null=True)
    doi = models.CharField(max_length=500, blank=True, null=True)
    book_gnd = models.CharField(max_length=500, blank=True, null=True)
    item_type = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="type fetched from Zotero"
    )
    book_type = models.ManyToManyField(SkosConcept, blank=True)

    def get_zotero_url(self):
        "Returns the objects URL pointing to its Zotero entry"
        try:
            base = "https://www.zotero.org/{}/".format(settings.Z_ID_TYPE)
            url = "{}{}/peter_handke_stage_texts/items/itemKey/{}".format(
                base, settings.Z_ID, self.zoterokey
            )
            return url
        except AttributeError:
            return "please provide Zotero settings"

    def __str__(self):
        return "{}, {}".format(self.author, self.title)


class Work(IdProvider):
    work_author = models.ManyToManyField(
        Person, blank=True, related_name="has_work_created")
    work_translator = models.ManyToManyField(
        Person, blank=True, related_name="has_work_translated"
    )
    title = models.CharField(
        verbose_name="Titel", max_length=500, blank=True, null=True,
        help_text="Geben Sie hier den Titel des publizierten Werks ein")
    alt_title = models.ManyToManyField(
        SkosConcept, blank=True, related_name="is_work_alt_title")
    creation_start_date = models.DateField(blank=True, null=True)
    creation_end_date = models.DateField(blank=True, null=True)
    start_date_sure = models.BooleanField(default=True)
    end_date_sure = models.BooleanField(default=True)
    creation_place = models.ManyToManyField(Place, blank=True)
    creation_place_sure = models.BooleanField(default=True)
    published_in = models.ManyToManyField(Book, blank=True)
    work_type = models.ManyToManyField(SkosConcept, blank=True)
    main_language = models.ForeignKey(
        SkosConcept, null=True, blank=True, related_name="language_of_work")
    has_translation = models.ForeignKey(
        'self', blank=True, null=True, related_name="is_translation_of"
    )

    def __str__(self):
        return "Work: {}".format(self.title)


class Speaker(IdProvider):
    name = models.CharField(max_length=500, blank=True, null=True)
    definition = models.CharField(max_length=500, blank=True, null=True)
    alt_name = models.ManyToManyField(SkosConcept, blank=True)

    def __str__(self):
        return "Speaker: {}".format(self.name)

class Quote(IdProvider):
    """Provides the context of quotes"""
    book_source = models.ForeignKey(Book, blank=True, null=True)
    startpage = models.IntegerField(blank=True)
    endpage = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    quote_type = models.ManyToManyField(SkosConcept, blank=True)
    part_of = models.ManyToManyField('self', blank=True)
    auto_trans = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return "{}".format(self.text)


class PartOfQuote(IdProvider):
    """A class modeling quotes"""
    text = models.CharField(blank=True, max_length=500)
    part_of = models.ManyToManyField(Quote, blank=True)
    source = models.ForeignKey(Work, blank=True, null=True)
    follows = models.ManyToManyField('self', blank=True, related_name='has_follower')
    translates = models.ManyToManyField('self', blank=True, related_name='has_translation')
    language = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='quote_language')
    partofquote_type = models.ManyToManyField(SkosConcept, blank=True, related_name='quote_type')
    speaker = models.ManyToManyField(Speaker, blank=True)

    def __str__(self):
        return "{}".format(self.text)
