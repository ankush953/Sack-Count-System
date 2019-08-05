from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company
from trucks.models import Truck, RecordTime
import datetime
from sacks.models import SackLoading, SackUnloading
import trucks.views as tv

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
	qs = Company.objects.all()
	isadmin = request.user.is_superuser
	context = {
		'company':qs,
		'title':'Home',
		'admin':isadmin
	}
	return render(request,'homepage.html',context=context)
	# return HttpResponse('Hello')

@login_required(login_url="login")
def query(request):
	# form = 
	# print(startdate,enddate)
	# print(request.POST)
	startdate = request.POST['startdate']
	enddate = request.POST['enddate']
	company = request.POST['company']
	# print(startdate,enddate, company)
	startdate = datetime.datetime.strptime(startdate,'%m/%d/%Y')
	enddate = datetime.datetime.strptime(enddate,'%m/%d/%Y')

	lqs = SackLoading.objects.filter(loading_date_time__gte=startdate,loading_date_time__lte=enddate)
	uqs = SackUnloading.objects.filter(unloading_date_time__gte=startdate,unloading_date_time__lte=enddate)
	recordtime = RecordTime.objects.filter(entry_date_time__gte=startdate,exit_date_time__lte=enddate)
	tv.startdate = startdate
	tv.enddate = enddate
	isadmin = request.user.is_superuser
	# print(recordtime)

	context = {
		'startdate':startdate,
		'enddate':enddate,
		'lqs':lqs,
		'uqs':uqs,
		'company':company,
		'title':'Query',
		'trucks':recordtime,
		'admin':isadmin
	}

	return render(request,'answer.html',context=context)

def about(request):
	context = {
		'admin':request.user.is_superuser
	}
	return render(request,'About.html',context=context)