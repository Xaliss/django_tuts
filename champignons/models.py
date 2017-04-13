from django.db import models
 

class Champ(models.Model):
	nomcommun = models.CharField(max_length=140)
	commentaire  = models.TextField()
	date  = models.DateTimeField()
	def __unicode__(self):
		return self.nomcommun
	def __str__(self):
		return self.nomcommun