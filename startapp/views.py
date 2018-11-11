from django.shortcuts import HttpResponse
import datetime
from django import template
from django.conf import settings
from django.shortcuts import HttpResponse ,render_to_response, render
def index(request):
    return HttpResponse("<p>Hello Django</p>")

def time(request):
    
    now = datetime.datetime.now()
#    t = template.loader.get_template('startapp/datetimeeeQ.html')
#c = template.Context({'now': now})
#   html = t.render({'now':now})
#  return HttpResponse(html)    
    return render(request,'startapp/datetime.html', {'now':now, 'template_name': 'startapp/nav.html', 'base_dir':settings.BASE_DIR})
def profile(request, username):
	return HttpResponse("<p>Profile page of {}</p>".format(username))


def books_catagory(request, catagory="catagory not defined"):
	return HttpResponse("<p> catagory is {}".format(catagory))
