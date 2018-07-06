from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm
from .models import Join, Tick_1yr_1hr
import os
from django.conf import settings
import uuid
import subprocess
from subprocess import Popen, PIPE, STDOUT
import csv
from django.core import serializers
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
import sys
from cStringIO import StringIO
from django.http import HttpResponse
import time



def get_ip(request):
	try:
		x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip


def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id


def share(request, ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		#referalls = Join.objects.filter(friend=referee)
		count = join_obj.referral.all().count()
		ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)

	except:
		raise Http404


def pychart(request, ref_id):
	join_obj = Join.objects.get(ref_id=ref_id)
	filepath = join_obj.filepath
	fullpath = os.path.join(settings.MEDIA_ROOT, filepath)
	logoutput = ""



	if request.method == 'POST':
		req_action = request.POST['action']
		req_data = request.POST['filedata'].strip()
		if req_action == "save":
			#print req_data
			with open (fullpath, "w") as myfile:
				myfile.write(req_data)



	#READ FILE AND PASS AS CONTEXT SO TEMPLATE CAN LOAD INTO EDITOR, also passed as string to "backtest"
	with open (fullpath, "r") as myfile:
			data=myfile.read().strip()





	try:
		##README!! THe code below needs to be refined to ONLY capture STD error and no other outputs
		p = subprocess.Popen(['python', os.path.join(os.getcwd(),'backtest.py'), data],  stdin=PIPE, stdout=PIPE, stderr=STDOUT)

		#logoutput = p.stdout.read() #Loop through results with .readline() and put quotes around each line + <br> for clearn reading in the log window
		for line in iter(p.stdout.readline, ''):
			logoutput += line + "</br>"


	except Exception as inst:
		d = inst
		logoutput = d







	#FORMAT, RENDER AND RETURN RESULTS
	context = {"ref_id": join_obj.ref_id, "filedata": data, "filename": filepath, "logoutput":logoutput}
	template = "pychart.html"
	return render(request, template, context)



def home(request):

	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print "The obj is %s" %(obj.email)
	except:
		obj = None


	form = JoinForm(request.POST or None)		# Get POST/Form data
	if form.is_valid():							# Check if form/data is valid
		new_join = form.save(commit=False)		# Assign form data to new_join object that we can manipulate

		# Manipulate new_join data here
		email = form.cleaned_data['email']

		new_join_existing, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_existing.ip_address = get_ip(request)
			#add our friend who referred us to our join model or related.
			if not obj == None:
				new_join_existing.friend = obj
			new_join_existing.ref_id = get_ref_id()
			new_join_existing.save()

		#redirect here
		return HttpResponseRedirect("/%s" %(new_join_existing.ref_id))


	context = {"form":form}
	template = "home.html"
	return render(request, template, context)



def pycharthome(request):

	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print "The obj is %s" %(obj.email)
	except:
		obj = None


	form = JoinForm(request.POST or None)		# Get POST/Form data
	if form.is_valid():							# Check if form/data is valid
		new_join = form.save(commit=False)		# Assign form data to new_join object that we can manipulate

		# Manipulate new_join data here
		email = form.cleaned_data['email']

		new_join_existing, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_existing.ip_address = get_ip(request)
			#add our friend who referred us to our join model or related.
			if not obj == None:
				new_join_existing.friend = obj
			new_join_existing.ref_id = get_ref_id()
			new_join_existing.save()


		#print Join.objects.filter(friend=obj).count()
		#print obj.referral.all().count()

		#redirect here
		return HttpResponseRedirect("pychart/%s" %(new_join_existing.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()						# Save the model/data.

	refDump = Join.objects.all().values_list('ref_id', flat=True)

	context = {"form":form, "refDump":refDump}
	template = "pycharthome.html"
	return render(request, template, context)

def importdata(request):
	filename = "bitstampUSD_1yr_1hr.csv"
	fullpath = os.path.join(settings.MEDIA_ROOT, filename)

	with open(fullpath) as f:
		reader = csv.reader(f)
		for row in reader:
			_, created = Tick_1yr_1hr.objects.get_or_create(
			ticktimestamp=row[0],
			tickopen=row[1],
			tickhigh=row[2],
			ticklow=row[3],
			tickclose=row[4]
			)
			print row[0]
			# creates a tuple of the new object or
			# current object and a boolean of if it was created

	context = {"result":fullpath}
	template = "import.html"
	return render(request, template, context)


def getTickData(request):

	ticks = []
	for tick in Tick_1yr_1hr.objects.filter(ticktimestamp__range=["2015-11-28", "2015-11-30"]):
		result = [int(time.mktime(tick.ticktimestamp.utctimetuple()))*1000, float(tick.tickclose)]
		ticks.append(result)

	tickdata = json.dumps(ticks, cls=DjangoJSONEncoder)


	return HttpResponse(tickdata, mimetype='application/json')
