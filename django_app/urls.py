from django.conf.urls.defaults import patterns, include, url

from django_app.views import hello

urlpatterns = patterns('',
    url(r'^fibo/(?P<n>\d+)$', 'django_app.views.fibo'),
)
