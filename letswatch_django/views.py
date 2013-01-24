from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context , RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from search.models import *

def sample_video_list():
	vids = Videos.objects.all()
	return vids
	
def show_trending():
	trends = Videos.objects.filter(pk__gt = 45)
	print len(trends)
	return trends

def home(request):
	vids = sample_video_list()
	trends = show_trending()
	return render_to_response('index.html' ,  {"vids" : vids , "trending" : trends}, context_instance=RequestContext(request))
