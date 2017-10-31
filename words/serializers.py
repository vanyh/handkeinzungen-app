from rest_framework import serializers
from .models import *


class GermanLemmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GermanLemma
        fields = "__all__"


class ForeignLemmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForeignLemma
        fields = "__all__"
