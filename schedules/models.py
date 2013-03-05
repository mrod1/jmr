from django.db import models
from courses.models import Course, Event

class CourseSchedule(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return unicode(self.course)

class EventSchedule(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    course_schedule = models.ForeignKey(CourseSchedule)
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return unicode(self.event)