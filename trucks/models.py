from django.db import models
from companies.models import Company
# Create your models here.
class Truck(models.Model):
	company = models.ForeignKey(Company,on_delete=models.CASCADE)
	entry_date_time = models.DateTimeField()
	exit_date_time = models.DateTimeField()
	Location = models.CharField(max_length = 40)
	truck_count = models.IntegerField()
	plateno = models.CharField(max_length=10)

	def __str__(self):
		return self.plateno