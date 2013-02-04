# Create your views here.

from django.shortcuts import render

from courses.models import Course

def index(request):
    latest_courses_list = Course.objects.order_by('start_date')[:5]
    context = {'latest_courses_list': latest_courses_list}
    return render(request, 'courses/index.html', context)
	
def detail(request, courses_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})

def results(request, courses_id):
    return HttpResponse("You're looking at the results of courses %s." % courses_id)

def vote(request, courses_id):
    return HttpResponse("You're voting on courses %s." % courses_id)