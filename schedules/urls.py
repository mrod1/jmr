from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from schedules.models import CourseSchedule

urlpatterns = patterns('',
#   url(r'^$', views.index, name='index'),
#    url(r'^(?P<courses_id>\d+)/$', views.detail, name='detail'),
    url(r'^$',
        ListView.as_view(
            queryset=CourseSchedule.objects.order_by('-start_date')[:5],
            context_object_name='latest_scheduled_courses_list',
            template_name='schedules/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=CourseSchedule,
            template_name='schedules/detail.html'),
        name='detail'),
)