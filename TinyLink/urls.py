from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tiny_link.views.home'),
    url(r'^(?P<id>\w+)$', 'tiny_link.views.link'),
    url(r'^(?P<id>\w+)/stats$', 'tiny_link.views.stats'),
)
