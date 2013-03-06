from django.http import HttpResponse
from courses.models import Course, Event, Lecturer
from schedules.models import CourseSchedule, EventSchedule

def home(request):
    content = "<h1>UCC Summer Courses!</h1>"
    content += "<a href=\"/\">Home</a>"
    content += " - "
    content += "<a href=\"schedules/\">Timetabled Courses</a>"
    content += " - "
    content += "<a href=\"courses/\">Courses we've run in the past</a>"
    content += " - "
    content += "<a href=\"account/login/\">Log in</a>"
    html = "<html><body>" + content + "</body></html>"
    return HttpResponse(html)