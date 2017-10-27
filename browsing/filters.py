import django_filters
from dal import autocomplete
from bib.models import *
from vocabs.models import SkosConcept

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
