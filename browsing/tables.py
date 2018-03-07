import django_tables2 as tables
from django_tables2.utils import A
from bib.models import *
from words.models import ForeignLemma, GermanLemma
from places.models import Place, AlternativeName
from django.utils.translation import ugettext


class GermanLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:germanlemma_detail',
        args=[A('pk')], verbose_name=ugettext('Lemma')
    )
    translation = tables.TemplateColumn(
        template_name='browsing/tables/germanlemma_foreignlemma.html', orderable=False, verbose_name=ugettext('Übersetzung')
    )

    class Meta:
        model = GermanLemma
        sequence = ('lemma', 'url', 'pos', 'translation')
        attrs = {"class": "table table-responsive table-hover"}


class ForeignLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:foreignlemma_detail',
        args=[A('pk')], verbose_name=ugettext('Lemma')
    )
    uebersetzung = tables.TemplateColumn(
        template_name='browsing/tables/foreignlemma_germanlemma.html', orderable=False, verbose_name=ugettext('Übersetzung')
    )

    class Meta:
        model = ForeignLemma
        sequence = ('lemma', 'uebersetzung', 'language')
        attrs = {"class": "table table-responsive table-hover"}


class PartOfQuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:partofquote_detail',
        args=[A('pk')], verbose_name='Text'
    )
    speaker = tables.TemplateColumn(
        template_name='browsing/tables/partofquote_speaker.html', orderable=True, verbose_name=ugettext('Figur')
    )
    source = tables.LinkColumn(
        'browsing:work_detail', args=[A('source.pk')], verbose_name=ugettext('Werk')
    )

    class Meta:
        model = PartOfQuote
        sequence = ('text', 'part_of', 'source', 'speaker')
        attrs = {"class": "table table-responsive table-hover"}


class QuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:quote_detail',
        args=[A('pk')], verbose_name='Text'
    )
    zitatsprache = tables.TemplateColumn(
        template_name='browsing/tables/quote_partofquote.html', orderable=True, verbose_name=ugettext('Sprache des Zitats')
    )

    class Meta:
        model = Quote
        sequence = ('text', 'book_source', 'zitatsprache')
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    first_name = tables.LinkColumn(
        'browsing:person_detail',
        args=[A('pk')], verbose_name=ugettext('Vorname')
    )

    class Meta:
        model = Person
        sequence = ('first_name', 'last_name', 'person_gnd')
        attrs = {"class": "table table-responsive table-hover"}


class WorkTable(tables.Table):
    title = tables.LinkColumn(
        'browsing:work_detail',
        args=[A('pk')], verbose_name=ugettext('Titel')
    )
    author = tables.TemplateColumn(
        template_name='browsing/tables/work_author.html', orderable=False, verbose_name=ugettext('Autor'))
    veroeffentlicht = tables.TemplateColumn(
        template_name='browsing/tables/work_book.html', orderable=False, verbose_name=ugettext('veröffentlicht in'))

    class Meta:
        model = Work
        sequence = ('title', 'veroeffentlicht', 'author', 'main_language', 'creation_start_date',)
        attrs = {"class": "table table-responsive table-hover"}


class BookTable(tables.Table):
    title = tables.LinkColumn(
        'browsing:book_detail',
        args=[A('pk')], verbose_name=ugettext('Titel')
    )

    class Meta:
        model = Book
        sequence = ('zoterokey', 'title',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    title = tables.LinkColumn(
        'places:place_detail',
        args=[A('pk')], verbose_name=ugettext('Titel')
    )

    class Meta:
        model = Place
        sequence = ('name', 'GeoNames',)
        attrs = {"class": "table table-responsive table-hover"}


class AlternativeNameTable(tables.Table):
    name = tables.LinkColumn(
        'places:alternativename_detail',
        args=[A('pk')], verbose_name=ugettext('Name')
    )

    class Meta:
        model = AlternativeName
        sequence = ('name',)
        attrs = {"class": "table table-responsive table-hover"}


class SpeakerTable(tables.Table):
    name = tables.LinkColumn(
        'browsing:speaker_detail',
        args=[A('pk')], verbose_name=ugettext('Name')
    )
    related_works = tables.TemplateColumn(
        template_name='browsing/tables/speaker_work.html', orderable=False)

    class Meta:
        model = Speaker
        sequence = ('name', 'definition', 'related_works')
        attrs = {"class": "table table-responsive table-hover"}
