import django_filters
from dal import autocomplete
from bib.models import *
from words.models import ForeignLemma, GermanLemma
from vocabs.models import SkosConcept
from places.models import Place, AlternativeName

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class GermanLemmaListFilter(django_filters.FilterSet):
    lemma = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=GermanLemma._meta.get_field('lemma').help_text,
        label=GermanLemma._meta.get_field('lemma').verbose_name
        )
    url = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=GermanLemma._meta.get_field('url').help_text,
        label=GermanLemma._meta.get_field('url').verbose_name
        )
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="POS"),
        help_text=GermanLemma._meta.get_field('pos').help_text,
        label=GermanLemma._meta.get_field('pos').verbose_name
        )

    class Meta:
        model = GermanLemma
        fields = [
            'id'
        ]


class ForeignLemmaListFilter(django_filters.FilterSet):
    lemma = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=ForeignLemma._meta.get_field('lemma').help_text,
        label=ForeignLemma._meta.get_field('lemma').verbose_name
        )
    german = django_filters.ModelMultipleChoiceFilter(
        queryset=GermanLemma.objects.all(),
        help_text=ForeignLemma._meta.get_field('german').help_text,
        label=ForeignLemma._meta.get_field('german').verbose_name
        )
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="POS"),
        help_text=ForeignLemma._meta.get_field('pos').help_text,
        label=ForeignLemma._meta.get_field('pos').verbose_name
        )
    language = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="Sprachen"),
        help_text=ForeignLemma._meta.get_field('language').help_text,
        label=ForeignLemma._meta.get_field('language').verbose_name
        )
    used_in = django_filters.ModelMultipleChoiceFilter(
        queryset=Quote.objects.all(),
        help_text=ForeignLemma._meta.get_field('used_in').help_text,
        label=ForeignLemma._meta.get_field('used_in').verbose_name
        )

    class Meta:
        model = ForeignLemma
        fields = [
            'id'
        ]


class PartOfQuoteListFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=PartOfQuote._meta.get_field('text').help_text,
        label=PartOfQuote._meta.get_field('text').verbose_name
        )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Book.objects.all(),
        help_text=PartOfQuote._meta.get_field('part_of').help_text,
        label=PartOfQuote._meta.get_field('part_of').verbose_name
        )
    language = django_filters.ModelMultipleChoiceFilter(
        queryset=Book.objects.all(),
        help_text=PartOfQuote._meta.get_field('language').help_text,
        label=PartOfQuote._meta.get_field('language').verbose_name
        )

    class Meta:
        model = PartOfQuote
        fields = [
            'id'
        ]


class QuoteListFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Quote._meta.get_field('text').help_text,
        label=Quote._meta.get_field('text').verbose_name
        )
    book_source = django_filters.ModelMultipleChoiceFilter(
        queryset=Book.objects.all(),
        help_text=Quote._meta.get_field('book_source').help_text,
        label=Quote._meta.get_field('book_source').verbose_name
        )

    class Meta:
        model = Quote
        fields = [
            'id'
        ]


class PersonListFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('last_name').help_text,
        label=Person._meta.get_field('last_name').verbose_name
        )
    first_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('first_name').help_text,
        label=Person._meta.get_field('first_name').verbose_name
        )
    person_gnd = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('person_gnd').help_text,
        label=Person._meta.get_field('person_gnd').verbose_name
        )

    class Meta:
        model = Person
        fields = [
            'id'
        ]


class WorkListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Work._meta.get_field('title').help_text,
        label=Work._meta.get_field('title').verbose_name
        )
    creation_start_date = django_filters.DateFromToRangeFilter()
    creation_end_date = django_filters.DateFromToRangeFilter()
    start_date_sure = django_filters.BooleanFilter()
    end_date_sure = django_filters.BooleanFilter()
    work_author = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=Work._meta.get_field('work_author').help_text,
        label=Work._meta.get_field('work_author').verbose_name
        )
    work_translator = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=Work._meta.get_field('work_translator').help_text,
        label=Work._meta.get_field('work_translator').verbose_name
        )
    alt_title = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="WorkAltTitle"),
        help_text=Work._meta.get_field('alt_title').help_text,
        label=Work._meta.get_field('alt_title').verbose_name
        )
    main_language = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title="Sprachen"),
        help_text=Work._meta.get_field('main_language').help_text,
        label=Work._meta.get_field('main_language').verbose_name
        )

    class Meta:
        model = Work
        fields = [
            'id'
        ]


class BookListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Book._meta.get_field('title').help_text,
        label=Book._meta.get_field('title').verbose_name
        )

    class Meta:
        model = Work
        fields = [
            'id'
        ]


class PlaceListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('name').help_text,
        label=Place._meta.get_field('name').verbose_name
        )
    geonames_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('geonames_id').help_text,
        label=Place._meta.get_field('geonames_id').verbose_name
        )
    alternative_name = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Place._meta.get_field('alternative_name').help_text,
        label=Place._meta.get_field('alternative_name').verbose_name
        )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field('part_of').help_text,
        label=Place._meta.get_field('part_of').verbose_name
        )

    class Meta:
        model = Place
        fields = [
            'id'
        ]
