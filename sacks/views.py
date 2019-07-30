from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company
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
	print(startdate,enddate, company)
	
	context = {
		'startdate':startdate,
		'enddate':enddate,
		'company':company,
		'title':'Query',
	}

	return render(request,'answer.html',context=context)