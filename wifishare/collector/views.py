from django.shortcuts import render
from map.models import *
import json 

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def collect_scan(request):
	scan = request.REQUEST.get('scan')
	scan = json.loads(scan)
	WiFiStore().store(scan)
	return HttpResponse(json.dumps({"operation":"scan", "success":True}))