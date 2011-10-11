from django.conf.urls.defaults import patterns, include, url

from django_fibo.views import hello
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_fibo.views.home', name='home'),
    # url(r'^django_fibo/', include('django_fibo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^fibo/(?P<n>\d+)$', 'django_fibo.views.fibo'),
)
