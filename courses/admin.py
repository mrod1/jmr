from django.contrib import admin
from courses.models import Course, Event

class EventInline(admin.StackedInline):
	model = Event
	extra = 1
	
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Course",               {'fields': ['name']}), 
		("Description", {'fields': ['description'], 'classes': ['collapse']}), 
		(None, {'fields': ['num_places']}),
		(None, {'fields': ['price']}),
        (None, {'fields': ['start_date']}),
    ]
    inlines = [EventInline]

admin.site.register(Course, CourseAdmin)