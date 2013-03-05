from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from schedules.models import CourseSchedule, EventSchedule
from courses.models import Course, Event
from django.contrib import admin

urlpatterns = patterns('',
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

class EventScheduleInline(admin.StackedInline):
    model = EventSchedule
    extra = 3
    fieldsets = [
        (None, {'fields': ['event', 'start_date', 'start_time']}), 
    ]
class CourseScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Timetable", {'fields': ['course', 'start_date', 'start_time']}), 
    ]
    inlines = [EventScheduleInline]
    save_as = True



admin.site.register(CourseSchedule, CourseScheduleAdmin)