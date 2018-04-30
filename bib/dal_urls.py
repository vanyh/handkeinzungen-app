from django.conf.urls import url
from .dal_views import SpeakerAltNameAC, QuoteBookSourceAC, QuoteQuoteTypeAC, QuotePartOfQuoteAC, QuoteSelfTranslationAC, PartOfQuotePartOfQuoteAC, PartOfQuoteSourceAC, PartOfQuoteFollowsAC, PartOfQuoteTranslationAC, PartOfQuoteLanguageAC, PartOfQuotePartOfQuoteTypeAC, PartOfQuoteSpeakerAC, WorkWorkAuthorAC, WorkWorkTranslatorAC, WorkAltTitleAC, WorkCreationPlaceAC, WorkPublishedInAC, WorkWorkTypeAC, WorkMainLanguageAC, WorkTranslationAC
from .models import Speaker, Book, Quote, Work, PartOfQuote, Person
from places.models import Place
from vocabs.models import SkosConcept


urlpatterns = [
    url(
        r'^speakeraltname-autocomplete/$', SpeakerAltNameAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='speakeraltname-autocomplete',
    ),
    url(
        r'^quotebooksource-autocomplete/$', QuoteBookSourceAC.as_view(
            model=Book, create_field='short_title',),
        name='quotebooksource-autocomplete',
    ),
    url(
        r'^quotequotetype-autocomplete/$', QuoteQuoteTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='quotequotetype-autocomplete',
    ),
    url(
        r'^quotepartofquote-autocomplete/$', QuotePartOfQuoteAC.as_view(
            model=Quote, create_field='text',),
        name='quotepartofquote-autocomplete',
    ),
    url(
        r'^quoteselftranslation-autocomplete/$', QuoteSelfTranslationAC.as_view(
            model=Quote, create_field='text',),
        name='quoteselftranslation-autocomplete',
    ),
    url(
        r'^partofquotepartofquote-autocomplete/$', PartOfQuotePartOfQuoteAC.as_view(
            model=Quote, create_field='text',),
        name='partofquotepartofquote-autocomplete',
    ),
    url(
        r'^partofquotesource-autocomplete/$', PartOfQuoteSourceAC.as_view(
            model=Work, create_field='title',),
        name='partofquotesource-autocomplete',
    ),
    url(
        r'^partofquotefollows-autocomplete/$', PartOfQuoteFollowsAC.as_view(
            model=PartOfQuote, create_field='text',),
        name='partofquotefollows-autocomplete',
    ),
    url(
        r'^partofquotetranslation-autocomplete/$', PartOfQuoteTranslationAC.as_view(
            model=PartOfQuote, create_field='text',),
        name='partofquotetranslation-autocomplete',
    ),
    url(
        r'^partofquotelanguage-autocomplete/$', PartOfQuoteLanguageAC.as_view(
            model=PartOfQuote, create_field='text',),
        name='partofquotelanguage-autocomplete',
    ),
    url(
        r'^partofquotepartofquotetype-autocomplete/$', PartOfQuotePartOfQuoteTypeAC.as_view(
            model=PartOfQuote, create_field='text',),
        name='partofquotepartofquotetype-autocomplete',
    ),
    url(
        r'^partofquotespeaker-autocomplete/$', PartOfQuoteSpeakerAC.as_view(
            model=Speaker, create_field='name',),
        name='partofquotespeaker-autocomplete',
    ),
    url(
        r'^workworkauthor-autocomplete/$', WorkWorkAuthorAC.as_view(
            model=Person, create_field='name',),
        name='workworkauthor-autocomplete',
    ),
    url(
        r'^workworktranslator-autocomplete/$', WorkWorkAuthorAC.as_view(
            model=Person, create_field='name',),
        name='workworktranslator-autocomplete',
    ),
    url(
        r'^workalttitle-autocomplete/$', WorkAltTitleAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='workalttitle-autocomplete',
    ),
    url(
        r'^workcreationplace-autocomplete/$', WorkCreationPlaceAC.as_view(
            model=Place, create_field='name',),
        name='workcreationplace-autocomplete',
    ),
    url(
        r'^workpublishedin-autocomplete/$', WorkPublishedInAC.as_view(
            model=Book, create_field='title',),
        name='workpublishedin-autocomplete',
    ),
    url(
        r'^workworktype-autocomplete/$', WorkWorkTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='workworktype-autocomplete',
    ),
    url(
        r'^workworktype-autocomplete/$', WorkWorkTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='workworktype-autocomplete',
    ),
    url(
        r'^workmainlanguage-autocomplete/$', WorkMainLanguageAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='workmainlanguage-autocomplete',
    ),
    url(
        r'^worktranslation-autocomplete/$', WorkTranslationAC.as_view(
            model=Work, create_field='title',),
        name='worktranslation-autocomplete',
    )
    ]
