from django.db import models
from django.utils.timesince import timesince

# Create your models here.

class MyQuotes(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	quote = models.CharField(max_length=255, blank=False)
	author = models.CharField(max_length=255, blank=False, null=True)

	def when_created(self):
		return timesince(self.created)

	class Meta:
		ordering = ["-created"]
