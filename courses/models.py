from django.db import models
from datetime import time
# New models.
class Course(models.Model):
    name = models.CharField(max_length=60)
    course_description = models.TextField()
    num_places = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=7)
    course_category = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Event(models.Model):
    courses = models.ForeignKey(Course)
    event_day_num = models.PositiveIntegerField()
    time_of_day = models.TimeField()
    duration = models.PositiveIntegerField()
    name = models.CharField(max_length=60)
    def end_time(self):
        time_to_add = time(minutes=self.duration)
        return (self.time_of_day + time_to_add)
    def __unicode__(self):
        return self.name