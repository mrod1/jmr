from django.db import models

# New models.
class Course(models.Model):
    course_name = models.CharField(max_length=60)
    course_description = models.TextField()
    num_places = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=7)

class Event(models.Model):
    event_name = models.CharField(max_length=60)
    event_day_num = models.PositiveIntegerField()
    time_of_day = models.TimeField()
    duration = models.TimeField()
    