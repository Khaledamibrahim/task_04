from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 120)
	cuisine = models.CharField(max_length = 50)
	dresscode = models.CharField(max_length = 30)
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	kids_allowed = models.CharField(max_length = 8)
	walk_in_allowed = models.CharField(max_length = 8)
	comments = models.TextField(max_length = 200)

	def __str__(self):
		return self.name