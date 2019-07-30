from django.db import models

# Create your models here.
def imagepath(request,filename):
	return request.company_name+'/logo/'+filename

class Company(models.Model):
	company_name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to=imagepath)
	establishment_year = models.DateField()
	contract_date_time = models.DateTimeField()
	contract_duration = models.IntegerField()
	location = models.CharField(max_length=100)
	number_of_trucks = models.IntegerField()

	def __str__(self):
		return  self.company_name
	
