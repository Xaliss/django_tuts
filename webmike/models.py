from django.db import models

class Livre(models.Model):
	titre = models.CharField(max_length=140)
	resume  = models.TextField()
	date  = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.titre
	def __str__(self):
		return self.titre
