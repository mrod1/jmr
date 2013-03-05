from django.db import models
# New models.
class Course(models.Model):
    name = models.CharField(max_length=60)
    course_description = models.TextField(blank=True)
    num_places = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=7)
    course_category = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Lecturer(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    title = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.first_name + " " + self.surname
    
    

class Event(models.Model):
    course = models.ForeignKey(Course)
    duration = models.PositiveIntegerField()
    name = models.CharField(max_length=60)
    lecturer = models.ForeignKey(Lecturer)
    def __unicode__(self):
        return self.name