from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^(?P<courses_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<courses_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<courses_id>\d+)/vote/$', views.vote, name='vote'),
)