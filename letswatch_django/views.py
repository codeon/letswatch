from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context , RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def home(request):
	return render_to_response('index.html' ,  {}, context_instance=RequestContext(request))
