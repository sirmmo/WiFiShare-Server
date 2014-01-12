from django.shortcuts import render_to_response
from map.models import *
# Create your views here.

def index(request):
	return render_to_response("index.html")

def heatmap(request):
	return 