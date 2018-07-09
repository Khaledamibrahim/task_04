from django.db import models

# Create your models here.
class restaurant(models.Model):
	Name = models.CharField(max_length = 120)
	Cuisne = models.CharField(max_length = 50)
	Dresscode = models.CharField(max_length = 30)
	Opening_Time = models.TimeField()
	Closing_Time = models.TimeField()
	Kids_allowed = models.CharField(max_length = 8)
	Walk_in_allowed = models.CharField(max_length = 8)
	Comments = models.TextField(max_length = 200)

	def __str__(self):
		return self.Name