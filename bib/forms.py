from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Person, Work, Quote, PartOfQuote, Book, Speaker
from words.models import GermanLemma, ForeignLemma
from django.utils.translation import ugettext


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = "__all__"
        widgets = {
            'work_author': autocomplete.ModelSelect2(url='bib-ac:workworkauthor-autocomplete'),
            'work_translator': autocomplete.ModelSelect2(url='bib-ac:workworktranslator-autocomplete'),
            'alt_title': autocomplete.ModelSelect2Multiple(url='bib-ac:workalttitle-autocomplete'),
            'creation_place': autocomplete.ModelSelect2(url='bib-ac:workcreationplace-autocomplete'),
            'published_in': autocomplete.ModelSelect2(url='bib-ac:workpublishedin-autocomplete'),
            'work_type': autocomplete.ModelSelect2(url='bib-ac:workworktype-autocomplete'),
            'main_language': autocomplete.ModelSelect2(url='bib-ac:workmainlanguage-autocomplete'),
            'has_translation': autocomplete.ModelSelect2(url='bib-ac:worktranslation-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        widgets = {
            'book_source': autocomplete.ModelSelect2(url='bib-ac:quotebooksource-autocomplete'),
            'quote_type': autocomplete.ModelSelect2(url='bib-ac:quotequotetype-autocomplete'),
            'part_of': autocomplete.ModelSelect2Multiple(url='bib-ac:quotepartofquote-autocomplete'),
            'auto_trans': autocomplete.ModelSelect2Multiple(url='bib-ac:quoteselftranslation-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class PartOfQuoteForm(forms.ModelForm):
    class Meta:
        model = PartOfQuote
        fields = "__all__"
        widgets = {
            'part_of': autocomplete.ModelSelect2(url='bib-ac:partofquotepartofquote-autocomplete'),
            'source': autocomplete.ModelSelect2(url='bib-ac:partofquotesource-autocomplete'),
            'follows': autocomplete.ModelSelect2(url='bib-ac:partofquotefollows-autocomplete'),
            'translates': autocomplete.ModelSelect2(url='bib-ac:partofquotetranslation-autocomplete'),
            'language': autocomplete.ModelSelect2(url='bib-ac:partofquotelanguage-autocomplete'),
            'partofquote_type': autocomplete.ModelSelect2(url='bib-ac:partofquotepartofquotetype-autocomplete'),
            'speaker': autocomplete.ModelSelect2(url='bib-ac:partofquotespeaker-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(PartOfQuoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class GermanLemmaForm(forms.ModelForm):
    class Meta:
        model = GermanLemma
        fields = "__all__"
        widgets = {
            'pos': autocomplete.ModelSelect2Multiple(url='words-ac:germanlemmapos-autocomplete'),
            'language': autocomplete.ModelSelect2(url='words-ac:germanlemmalanguage-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(GermanLemmaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class ForeignLemmaForm(forms.ModelForm):
    class Meta:
        model = ForeignLemma
        fields = "__all__"
        widgets = {
            'german': autocomplete.ModelSelect2Multiple(url='words-ac:foreignlemmagerman-autocomplete'),
            'pos': autocomplete.ModelSelect2Multiple(url='words-ac:foreignlemmapos-autocomplete'),
            'language': autocomplete.ModelSelect2(url='words-ac:foreignlemmalanguage-autocomplete'),
            'used_in': autocomplete.ModelSelect2Multiple(url='words-ac:foreignlemmausedin-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(ForeignLemmaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = "__all__"
        widgets = {
            'alt_name': autocomplete.ModelSelect2Multiple(url='bib-ac:speakeraltname-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(SpeakerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', ugettext("save")),)
