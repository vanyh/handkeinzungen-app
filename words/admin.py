from django.contrib import admin
from .models import GermanLemma, ForeignLemma

admin.site.register(GermanLemma)
admin.site.register(ForeignLemma)

# Register your models here.
