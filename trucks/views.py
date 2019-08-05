from django.shortcuts import render
from trucks.models import Truck, RecordTime
from sacks.models import Sack, SackLoading, SackUnloading
startdate = None
enddate = None
# Create your views here.
def showtruck(request):
    recordtime = RecordTime.objects.filter(entry_date_time__gte=startdate,
    exit_date_time__lte=enddate)
    lqs = SackLoading.objects.filter(loading_date_time__gte=startdate,loading_date_time__lte=enddate)
    uqs = SackUnloading.objects.filter(unloading_date_time__gte=startdate,unloading_date_time__lte=enddate)
    isadmin = request.user.is_superuser
    print(lqs,uqs)
    context = {
        'lqs':lqs,
        'uqs':uqs,
        'admin':isadmin
    }
    return render(request,'truck.html',context=context)