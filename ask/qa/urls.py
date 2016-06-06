from django.conf.urls import url
from .views import (
    test
)

urlpatterns = [
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<question_id>[0-9]+)/$', test),
    url(r'^ask/.*$', test),
    url(r'^popular/$', test),
    url(r'^new/$', test),
]