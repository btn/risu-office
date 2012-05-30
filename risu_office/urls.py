from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'vulnerability.views.json', name='json'),
    url(r'^table/$', 'vulnerability.views.table', name='table'),
)

