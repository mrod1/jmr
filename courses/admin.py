from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from courses.models import Course, Event, Lecturer
from django.contrib import admin

urlpatterns = patterns('',
#   url(r'^$', views.index, name='index'),
#    url(r'^(?P<courses_id>\d+)/$', views.detail, name='detail'),
    url(r'^$',
        ListView.as_view(
            queryset=Course.objects.order_by('-name')[:5],
            context_object_name='alphabetical_courses_list',
            template_name='courses/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Course,
            template_name='courses/detail.html'),
        name='detail'),
)

class EventInline(admin.StackedInline):
    model = Event
    extra = 1
class LecturerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Lecturer', {'fields': ['title','first_name', 'surname']}),
        ('Contact Email (optional)', {'fields': ['email']})
    ]
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Course",               {'fields': ['name']}), 
        ("Description", {'fields': ['course_description'], 'classes': ['collapse']}), 
        (None, {'fields': ['num_places']}),
        (None, {'fields': ['price']}),
    ]
    inlines = [EventInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)