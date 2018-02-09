import django_tables2 as tables
from django_tables2.utils import A
from bib.models import *
from words.models import ForeignLemma, GermanLemma
from places.models import Place, AlternativeName


class GermanLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:germanlemma_detail',
        args=[A('pk')], verbose_name='Lemma'
    )
    translation = tables.TemplateColumn(
        template_name='browsing/tables/germanlemma_foreignlemma.html', orderable=False
    )

    class Meta:
        model = GermanLemma
        sequence = ('lemma', 'url', 'pos', 'translation')
        attrs = {"class": "table table-responsive table-hover"}


class ForeignLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:foreignlemma_detail',
        args=[A('pk')], verbose_name='Lemma'
    )
    uebersetzung = tables.TemplateColumn(
        template_name='browsing/tables/foreignlemma_germanlemma.html', orderable=False
    )

    class Meta:
        model = ForeignLemma
        sequence = ('id', 'lemma', 'uebersetzung')
        attrs = {"class": "table table-responsive table-hover"}


class PartOfQuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:partofquote_detail',
        args=[A('pk')], verbose_name='Text'
    )
    speaker = tables.TemplateColumn(
        template_name='browsing/tables/partofquote_speaker.html', orderable=False
    )

    class Meta:
        model = PartOfQuote
        sequence = ('text', 'part_of', 'speaker')
        attrs = {"class": "table table-responsive table-hover"}


class QuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:quote_detail',
        args=[A('pk')], verbose_name='Text'
    )

    class Meta:
        model = Quote
        sequence = ('text', 'book_source')
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    first_name = tables.LinkColumn(
        'browsing:person_detail',
        args=[A('pk')], verbose_name='Vorname'
    )

    class Meta:
        model = Person
        sequence = ('first_name', 'last_name', 'person_gnd')
        attrs = {"class": "table table-responsive table-hover"}


class WorkTable(tables.Table):
    title = tables.LinkColumn(
        'browsing:work_detail',
        args=[A('pk')], verbose_name='Titel'
    )
    author = tables.TemplateColumn(
        template_name='browsing/tables/work_author.html', orderable=False)

    class Meta:
        model = Work
        sequence = ('title', 'author', 'main_language', 'creation_start_date',)
        attrs = {"class": "table table-responsive table-hover"}


class BookTable(tables.Table):
    title = tables.LinkColumn(
        'browsing:book_detail',
        args=[A('pk')], verbose_name='Titel'
    )

    class Meta:
        model = Book
        sequence = ('zoterokey', 'title',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    title = tables.LinkColumn(
        'places:place_detail',
        args=[A('pk')], verbose_name='Titel'
    )

    class Meta:
        model = Place
        sequence = ('name', 'GeoNames',)
        attrs = {"class": "table table-responsive table-hover"}


class AlternativeNameTable(tables.Table):
    name = tables.LinkColumn(
        'places:alternativename_detail',
        args=[A('pk')], verbose_name='Name'
    )

    class Meta:
        model = AlternativeName
        sequence = ('name',)
        attrs = {"class": "table table-responsive table-hover"}


class SpeakerTable(tables.Table):
    name = tables.LinkColumn(
        'browsing:speaker_detail',
        args=[A('pk')], verbose_name='Name'
    )
    related_works = tables.TemplateColumn(
        template_name='browsing/tables/speaker_work.html', orderable=False)

    class Meta:
        model = Speaker
        sequence = ('name', 'definition', 'related_works')
        attrs = {"class": "table table-responsive table-hover"}
