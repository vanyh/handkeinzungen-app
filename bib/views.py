import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from .models import Book, Person, Work, Quote, PartOfQuote, Book
from words.models import GermanLemma, ForeignLemma
from .forms import PersonForm, WorkForm, QuoteForm, PartOfQuoteForm, GermanLemmaForm, ForeignLemmaForm, BookForm
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings


def sync_zotero(request):
    """ renders a simple template with a button to trigger sync_zotero_action function """
    context = {}
    try:
        context['base_url'] = settings.Z_COLLECTION_URL
        context['collection_title'] = settings.Z_TITLE
    except:
        context['base_url'] = ''
        context['collection_title'] = 'PLEASE PROVIDE TITEL IN SETTINGS FILE'
    return render(request, 'bib/synczotero.html', context)


class PersonUpdate(UpdateView):

    model = Person
    form_class = PersonForm
    template_name = 'bib/person_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonCreate(CreateView):

    model = Person
    form_class = PersonForm
    template_name = 'bib/person_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_persons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class WorkUpdate(UpdateView):

    model = Work
    form_class = WorkForm
    template_name = 'bib/work_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkUpdate, self).dispatch(*args, **kwargs)


class WorkCreate(CreateView):

    model = Work
    form_class = WorkForm
    template_name = 'bib/work_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkCreate, self).dispatch(*args, **kwargs)


class WorkDelete(DeleteView):
    model = Work
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_works')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkDelete, self).dispatch(*args, **kwargs)


class QuoteUpdate(UpdateView):

    model = Quote
    form_class = QuoteForm
    template_name = 'bib/quote_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(QuoteUpdate, self).dispatch(*args, **kwargs)


class QuoteCreate(CreateView):

    model = Quote
    form_class = QuoteForm
    template_name = 'bib/quote_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(QuoteCreate, self).dispatch(*args, **kwargs)


class QuoteDelete(DeleteView):
    model = Quote
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_quotes')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(QuoteDelete, self).dispatch(*args, **kwargs)


class PartOfQuoteUpdate(UpdateView):

    model = PartOfQuote
    form_class = PartOfQuoteForm
    template_name = 'bib/partofquote_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartOfQuoteUpdate, self).dispatch(*args, **kwargs)


class PartOfQuoteCreate(CreateView):

    model = PartOfQuote
    form_class = PartOfQuoteForm
    template_name = 'bib/partofquote_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartOfQuoteCreate, self).dispatch(*args, **kwargs)


class PartOfQuoteDelete(DeleteView):
    model = PartOfQuote
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_partofquotes')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PartOfQuoteDelete, self).dispatch(*args, **kwargs)


class GermanLemmaUpdate(UpdateView):
    model = GermanLemma
    form_class = GermanLemmaForm
    template_name = 'bib/germanlemma_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GermanLemmaUpdate, self).dispatch(*args, **kwargs)


class GermanLemmaCreate(CreateView):
    model = GermanLemma
    form_class = GermanLemmaForm
    template_name = 'bib/germanlemma_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GermanLemmaCreate, self).dispatch(*args, **kwargs)


class GermanLemmaDelete(DeleteView):
    model = GermanLemma
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_germanlemmas')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GermanLemmaDelete, self).dispatch(*args, **kwargs)


class ForeignLemmaUpdate(UpdateView):
    model = ForeignLemma
    form_class = ForeignLemmaForm
    template_name = 'bib/foreignlemma_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ForeignLemmaUpdate, self).dispatch(*args, **kwargs)


class ForeignLemmaCreate(CreateView):
    model = ForeignLemma
    form_class = ForeignLemmaForm
    template_name = 'bib/foreignlemma_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ForeignLemmaCreate, self).dispatch(*args, **kwargs)


class ForeignLemmaDelete(DeleteView):
    model = ForeignLemma
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_foreignlemmas')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ForeignLemmaDelete, self).dispatch(*args, **kwargs)


class BookUpdate(UpdateView):

    model = Book
    form_class = BookForm
    template_name = 'bib/book_edit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BookUpdate, self).dispatch(*args, **kwargs)


class BookDelete(DeleteView):
    model = Book
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_books')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BookDelete, self).dispatch(*args, **kwargs)


@login_required
def sync_zotero_action(request):
    """ fetches the last n items form zoter and syncs it with the bib entries in defc-db"""
    root = "https://api.zotero.org/"
    try:
        params = "{}/{}/collections/{}/items/top?v=3&key={}".format(
            settings.Z_ID_TYPE, settings.Z_ID, settings.Z_COLLECTION, settings.Z_API_KEY
        )
    except AttributeError as err:
        context = {}
        context['error'] = "{}".format(err)
        return render(request, 'bib/synczotero_action.html', context)
    url = root + params + "&sort=dateModified&limit=25"
    print(url)
    books_before = len(Book.objects.all())
    try:
        r = requests.get(url)
        error = "No errors from ZoteroAPI"
    except:
        error = "aa! errors! The API didn´t response with a proper json-file"

    response = r.json()
    failed = []
    saved = []
    for x in response:
        try:
            x["data"]["creators"][0]
            try:
                x["data"]["creators"][0]["name"]
                name = x["data"]["creators"][0]["name"]
            except:
                firstname = x["data"]["creators"][0]["firstName"]
                lastname = x["data"]["creators"][0]["lastName"]
                name = "{}, {}".format(lastname, firstname)
        except:
            name = "no name provided"
        NewBook = Book(
            zoterokey=x["data"]["key"], item_type=x["data"]["itemType"],
            author=name,
            title=x["data"]["title"],
            short_title=x["data"]["shortTitle"]
        )
        try:
            NewBook.save()
            saved.append(NewBook)
        except:
            failed(x['data'])
    books_after = len(Book.objects.all())
    context = {}
    context["error"] = error
    context["saved"] = saved
    context["failed"] = failed
    context["books_before"] = [books_before]
    context["books_after"] = [books_after]
    return render(request, 'bib/synczotero_action.html', context)
