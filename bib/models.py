from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from idprovider.models import IdProvider
from vocabs.models import SkosConcept
from places.models import Place
from .helper_functions import create_tag


class Person(IdProvider):
    """Eine Person, zum Beispiel die Verfasserin eines Werks."""
    first_name = models.CharField(max_length=100, blank=True, null=True,
    verbose_name="Vorname der Person")
    last_name = models.CharField(max_length=100, blank=True, null=True,
    verbose_name="Nachname der Person")
    person_gnd = models.CharField(max_length=100, blank=True, null=True,
    verbose_name="GND-ID der Person")

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_persons')

    def get_next(self):
        next = Person.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Person.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('browsing:person_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Book(models.Model):
    """Bibliographische Informationen zu einem publizierten Buch."""
    zoterokey = models.CharField(
        verbose_name="Zoterokey", primary_key=True, max_length=100, blank=True,
        help_text="Zoterokey des bibliographischen Eintrags aus der Zoterolibrary 'Peter Handke stage texts'")
    item_type = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name="Item type")
    author = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="Autor*innenname laut Zotero-Eintrag"
    )
    book_author = models.ManyToManyField(
        Person, blank=True, verbose_name="Autor*innenname")
    title = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Titel des Werks")
    siglum = models.CharField(
        verbose_name="Sigle", max_length=500, blank=True, null=True,
        help_text="Sigle des publizierten Werks (laut Handkeonline)")
    publication_title = models.CharField(max_length=100, blank=True, null=True)
    short_title = models.CharField(max_length=500, blank=True, null=True)
    publication_year = models.IntegerField(
        blank=True, null=True, verbose_name="Jahr der Veröffentlichung")
    pub_place = models.ManyToManyField(
        Place, blank=True, verbose_name="Ort der Veröffentlichung")
    book_gnd = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="GND-ID des Buchs")
    item_type = models.CharField(
        max_length=500, blank=True, null=True,
        verbose_name="Item type laut Zotero-Eintrag"
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
    """Ein Werk an sich (unabhängig von seiner Nicht-/Publikation)"""
    work_author = models.ManyToManyField(
        Person, blank=True, related_name="has_work_created",
        verbose_name="Autor*in des Werks")
    work_translator = models.ManyToManyField(
        Person, blank=True, related_name="has_work_translated",
        verbose_name="Übersetzer*in des werks"
    )
    title = models.CharField(
        verbose_name="Titel des Werks", max_length=500, blank=True, null=True)
    alt_title = models.ManyToManyField(
        SkosConcept, blank=True, related_name="is_work_alt_title", verbose_name="Titelvarianten")
    creation_start_date = models.DateField(blank=True, null=True, verbose_name="entstanden von")
    creation_end_date = models.DateField(blank=True, null=True, verbose_name="entstanden bis")
    start_date_sure = models.BooleanField(default=True, verbose_name="Anfangsdatum gesichert")
    end_date_sure = models.BooleanField(default=True, verbose_name="Enddatum gesichert")
    creation_place = models.ManyToManyField(Place, blank=True, verbose_name="Entstehungsort")
    creation_place_sure = models.BooleanField(default=True, verbose_name="Entstehungsort gesichert")
    published_in = models.ManyToManyField(
        Book, blank=True, related_name="publication_of_work", verbose_name="veröffentlicht in")
    work_type = models.ManyToManyField(SkosConcept, blank=True, verbose_name="Werktyp")
    main_language = models.ForeignKey(
        SkosConcept, null=True, blank=True, related_name="language_of_work",
        verbose_name="dominante Schreibsprache")
    has_translation = models.ForeignKey(
        'self', blank=True, null=True, related_name="is_translation_of", verbose_name="Übersetzung"
    )

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_works')

    def get_next(self):
        next = Work.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Work.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "Work: {}".format(self.title)

    def get_absolute_url(self):
        return reverse('browsing:work_detail', kwargs={'pk': self.id})


class Speaker(IdProvider):
    """Figur, die spricht"""
    name = models.CharField(max_length=500, blank=True, null=True, verbose_name="Figurenname")
    definition = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="weitere Informationen zur Figur"
    )
    alt_name = models.ManyToManyField(
        SkosConcept, blank=True, verbose_name="alternative Figurenbezeichnungen"
    )

    def __str__(self):
        return "Speaker: {}".format(self.name)


class Quote(IdProvider):
    """ein Zitat, das auch Kontext zu fremdsprachigen Textstellen beinhaltet"""
    book_source = models.ForeignKey(
        Book, blank=True, null=True, related_name="has_quotes", verbose_name="Quelle"
    )
    startpage = models.IntegerField(blank=True, verbose_name="Seite (von)")
    endpage = models.IntegerField(blank=True, verbose_name="Seite (bis)")
    text = models.TextField(blank=True, verbose_name="Text")
    quote_type = models.ManyToManyField(SkosConcept, blank=True, verbose_name="Zitattyp")
    part_of = models.ManyToManyField(
        'self', blank=True, verbose_name="Teil von Zitat",
        help_text="Dieses Zitat ist Teil eines umfangreicheren Zitats")
    auto_trans = models.ManyToManyField('self', blank=True, verbose_name="Selbstübersetzung")

    def serialize_quote(self):
        """ retuns the quote's text with tagged part of quote chunks"""
        partofs = PartOfQuote.objects.filter(part_of=self)
        quote = self.text
        for x in partofs:
            quote = quote.replace(x.text, create_tag(x))
        return quote

    def get_next(self):
        next = Quote.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Quote.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_quotes')

    def __str__(self):
        return "{}".format(self.text)

    def get_absolute_url(self):
        return reverse('browsing:quote_detail', kwargs={'pk': self.id})


class PartOfQuote(IdProvider):
    """fremdsprachiger Zitatteil"""
    text = models.CharField(blank=True, max_length=500, verbose_name="Text")
    part_of = models.ForeignKey(
        Quote, blank=True, null=True, related_name="has_chunks",
        verbose_name="Teil von Zitat",
        help_text="Dieses Teilzitat ist Teil eines umfangreicheren Zitats")
    source = models.ForeignKey(Work, blank=True, null=True, verbose_name="Quelle")
    follows = models.ForeignKey(
        'self', blank=True, null=True, related_name='has_follower',
        verbose_name="folgt auf", help_text="Dieses Teilzitat folgt einem anderen")
    translates = models.ManyToManyField(
        'self', blank=True, related_name='has_translation', verbose_name="Übersetzung",
        help_text="Dieses Teilzitat hat eine Übersetzung in unmittelbarer Umgebung innerhalb des Texts"
    )
    correct_translation_sure = models.BooleanField(
        default=True, verbose_name="Übersetzung korrekt")
    language = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='quote_language', verbose_name="Sprache")
    partofquote_type = models.ManyToManyField(
        SkosConcept, blank=True, related_name='quote_type', verbose_name="Teilzitattyp")
    speaker = models.ManyToManyField(Speaker, blank=True, verbose_name="Figur")

    def get_absolute_url(self):
        return reverse('browsing:partofquote_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_partofquotes')

    def get_next(self):
        next = PartOfQuote.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = PartOfQuote.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{} - {}".format(self.id, self.text)
