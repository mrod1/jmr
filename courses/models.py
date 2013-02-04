from django.db import models

# Create your models here.

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	num_places = models.PositiveIntegerField()
	price = models.FloatField()
	start_date = models.DateField()
	def __unicode__(self):
		return self.name

class Event(models.Model):
	courses = models.ForeignKey(Course)
	event_name = models.CharField(max_length=100)
	event_time = models.DateTimeField('time of event')
	duration = models.PositiveIntegerField('duration in minutes')
	def __unicode__(self):
		return self.event_name
