import django_tables2 as tables
from django_tables2.utils import A
from bib.models import *


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
