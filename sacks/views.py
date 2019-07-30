from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company
import datetime
from sacks.models import SackLoading, SackUnloading
# Create your views here.
def home(request):
	qs = Company.objects.all()
	context = {
		'company':qs,
		'title':'Home',
	}
	return render(request,'homepage.html',context=context)
	# return HttpResponse('Hello')

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

	context = {
		'startdate':startdate,
		'enddate':enddate,
		'lqs':lqs,
		'uqs':uqs,
		'company':company,
		'title':'Query',
	}

	return render(request,'answer.html',context=context)