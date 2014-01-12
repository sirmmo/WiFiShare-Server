from django.shortcuts import render
from map.models import *

from django.http import HttpResponse

def locate(request):
	ident = request.get('ident')
	pattern = request.get('pattern')
	WiFiStore().locate(ident, pattern)
	return HttpResponse()