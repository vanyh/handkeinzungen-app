from django.contrib import admin
from .models import Book, PartOfQuote, Quote, Work, Speaker, Person

admin.site.register(Book)
admin.site.register(PartOfQuote)
admin.site.register(Quote)
admin.site.register(Work)
admin.site.register(Speaker)
admin.site.register(Person)
