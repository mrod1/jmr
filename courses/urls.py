from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from courses.models import Course

urlpatterns = patterns('',
#   url(r'^$', views.index, name='index'),
#    url(r'^(?P<courses_id>\d+)/$', views.detail, name='detail'),
    url(r'^$',
        ListView.as_view(
            queryset=Course.objects.order_by('-name')[:5],
            context_object_name='latest_courses_list',
            template_name='courses/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Course,
            template_name='courses/detail.html'),
        name='detail'),
)