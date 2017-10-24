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
    # lemma__name = django_filters.CharFilter(
    #     lookup_expr='icontains',
    #     help_text=Lemma._meta.get_field('name').help_text,
    #     label=Lemma._meta.get_field('name').verbose_name
    #     )
    # lemma__pos = django_filters.ModelMultipleChoiceFilter(
    #     queryset = SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
    #     help_text=Lemma._meta.get_field('pos').help_text,
    #     label=Lemma._meta.get_field('pos').verbose_name
    #     )
    # pos = django_filters.ModelMultipleChoiceFilter(
    #     queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
    #     help_text=Work._meta.get_field('pos').help_text,
    #     label=Work._meta.get_field('pos').verbose_name
    #     )
    # label = django_filters.ModelMultipleChoiceFilter(
    #     queryset=WorkLabel.objects.all(),
    #     help_text=Work._meta.get_field('label').help_text,
    #     label=Work._meta.get_field('label').verbose_name
    #     )
    # medial_suffix = django_filters.CharFilter(
    #     lookup_expr='icontains',
    #     help_text=Work._meta.get_field('medial_suffix').help_text,
    #     label=Work._meta.get_field('medial_suffix').verbose_name
    #     )
    # final_suffix = django_filters.CharFilter(
    #     lookup_expr='icontains',
    #     help_text=Work._meta.get_field('final_suffix').help_text,
    #     label=Work._meta.get_field('final_suffix').verbose_name
    #     )

    class Meta:
        model = Work
        fields = [
            'id'
        ]
