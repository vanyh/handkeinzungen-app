from django.conf.urls import url
from . import detail_views
from . import views

urlpatterns = [
    url(r'works/$', views.WorkListView.as_view(), name='browse_works'),
    url(r'^work/(?P<pk>[0-9]+)$', detail_views.WorkDetailView.as_view(),
        name='work_detail'),
]
