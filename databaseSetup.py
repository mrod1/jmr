from courses.models import Course, Event

Course.objects.all()

from django.utils import timezone

p = Course(name="Population and Community Ecology", description="Sampling Terrestrial, Marine and Freshwater Ecosystems. Identification of Species. Analysis of Data. Phytosociology. Vegetation Analysis and Species Diversity.", num_places=50, price=990.90, start_date=timezone.now())

Course.objects.all()

p = Course.objects.get(pk=1)

p.events_set.all()

from django.utils import timezone

p.events_set.create(event_name='Lecture about population', event_time=timezone.now(), duration = 60)

p.events_set.create(event_name='Lecture about ecology', event_time=timezone.now(), duration = 90)