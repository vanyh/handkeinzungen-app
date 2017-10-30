import django_tables2 as tables
from django_tables2.utils import A
from bib.models import *
from words.models import ForeignLemma, GermanLemma


class GermanLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:germanlemma_detail',
        args=[A('pk')], verbose_name='Lemma'
    )
    language = tables.Column()

    class Meta:
        model = GermanLemma
        sequence = ('id', 'lemma',)
        attrs = {"class": "table table-responsive table-hover"}


class ForeignLemmaTable(tables.Table):
    lemma = tables.LinkColumn(
        'browsing:foreignlemma_detail',
        args=[A('pk')], verbose_name='Lemma'
    )
    language = tables.Column()

    class Meta:
        model = ForeignLemma
        sequence = ('id', 'lemma',)
        attrs = {"class": "table table-responsive table-hover"}


class PartOfQuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:partofquote_detail',
        args=[A('pk')], verbose_name='Text'
    )
    part_of = tables.Column()
    language = tables.Column()

    class Meta:
        model = PartOfQuote
        sequence = ('text', 'part_of')
        attrs = {"class": "table table-responsive table-hover"}


class QuoteTable(tables.Table):
    text = tables.LinkColumn(
        'browsing:quote_detail',
        args=[A('pk')], verbose_name='Text'
    )
    book_source = tables.Column()

    class Meta:
        model = Quote
        sequence = ('text', 'book_source')
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    first_name = tables.LinkColumn(
        'browsing:person_detail',
        args=[A('pk')], verbose_name='Vorname'
    )
    last_name = tables.Column()
    person_gnd = tables.Column()

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
    main_language = tables.Column()
    creation_start_date = tables.Column()

    class Meta:
        model = Work
        sequence = ('title', 'author', 'main_language', 'creation_start_date',)
        attrs = {"class": "table table-responsive table-hover"}
