from django.conf.urls.defaults import patterns, url

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from mongonaut import views

urlpatterns = patterns('',
    url(
        regex=r'^2/(?P<app_label>[_\-\w]+)/(?P<document_name>[_\-\w]+)/$',
        view=views.DocumentListView.as_view(),
        name="document_list"
    )
)

