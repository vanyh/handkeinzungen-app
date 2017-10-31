from rest_framework import viewsets
from .serializers import *
from .models import *


class GermanLemmaViewSet(viewsets.ModelViewSet):
    queryset = GermanLemma.objects.all()
    serializer_class = GermanLemmaSerializer


class ForeignLemmaViewSet(viewsets.ModelViewSet):
    queryset = ForeignLemma.objects.all()
    serializer_class = ForeignLemmaSerializer
