from django.conf.urls import url
from .dal_views import GermanLemmaAC
from .models import GermanLemma


urlpatterns = [
    url(
        r'^germanlemma-autocomplete/$', GermanLemmaAC.as_view(
            model=GermanLemma, create_field='lemma',),
        name='germanlemma-autocomplete',
    ),
]
