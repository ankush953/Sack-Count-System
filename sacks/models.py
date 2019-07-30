from django.db import models
from trucks.models import Truck
# Create your models here.
def loadingimagepath(request,filename):
	return 'sacks/loading/'+str(request.loading_date_time.date())+'/'+str(request.loading_date_time.time())+'-'+filename

def unloadingimagepath(request,filename):
	return 'sacks/unloading/'+str(request.unloading_date_time.date())+'/'+str(request.unloading_date_time.time())+'-'+filename

class Sack(models.Model):
	truck = models.ForeignKey(Truck,on_delete=models.CASCADE)

	def __str__(self):
		return self.truck.plateno+'-'+str(self.id)

class SackLoading(Sack):
	loading_date_time = models.DateTimeField()
	sack_img = models.ImageField(upload_to=loadingimagepath)

class SackUnloading(Sack):
	unloading_date_time = models.DateTimeField()
	sack_img = models.ImageField(upload_to=unloadingimagepath)