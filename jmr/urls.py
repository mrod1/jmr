from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.views.generic import DetailView, ListView
from courses.models import Course
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'jmr.views.home', name='home'),
    # url(r'^jmr/', include('jmr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^schedules/', include('schedules.urls', namespace="schedules")),
)
