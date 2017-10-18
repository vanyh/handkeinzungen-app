from django.contrib import admin
from .models import Book, TextChunk, Quote

admin.site.register(Book)
admin.site.register(TextChunk)
admin.site.register(Quote)
