from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^altnames/detail/(?P<pk>[0-9]+)$', views.AlternativeNameDetailView.as_view(),
        name='alternativename_detail'),
    url(r'^altnames/edit/(?P<pk>[0-9]+)$', views.AlternativeNameUpdate.as_view(),
        name='alternativename_edit'),
    url(r'^altnames/create/$', views.AlternativeNameCreate.as_view(),
        name='alternativename_create'),
    url(r'^altnames/delete/(?P<pk>[0-9]+)$', views.AlternativeNameDelete.as_view(),
        name='alternativename_delete'),
    url(r'^$', views.PlaceListView.as_view(), name='place_list'),
    url(r'^create/$', views.create_place, name='place_create'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_place, name='place_edit'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.PlaceDetailView.as_view(), name='place_detail'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete')
]
