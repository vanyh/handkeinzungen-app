import django_tables2 as tables
from django_tables2.utils import A
from bib.models import *


class WorkTable(tables.Table):
    id = tables.LinkColumn(
        'browsing:work_detail',
        args=[A('pk')], verbose_name='ID'
    )
    title = tables.LinkColumn(
        'browsing:work_detail',
        args=[A('pk')], verbose_name='Titel'
    )
    # lemma = tables.RelatedLinkColumn()
    # cluster = tables.RelatedLinkColumn()
    # label = tables.RelatedLinkColumn()
    # date = tables.RelatedLinkColumn(accessor='text_source.mean_date', verbose_name='Date')

    class Meta:
        model = Work
        sequence = ('title', 'id')
        attrs = {"class": "table table-responsive table-hover"}
