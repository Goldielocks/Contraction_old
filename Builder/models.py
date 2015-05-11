from django.db import models
from django import forms
from mptt.models import MPTTModel, TreeForeignKey

class Citation(models.Model):
	name = models.CharField(max_length=60)
	link = models.CharField(max_length=80)

	def __unicode__(self):
		return self.name


class Case(MPTTModel):
	name = models.CharField(max_length=60, db_index = True, blank=True)
	value = models.CharField(max_length=2000, blank=True	)	
	citations = models.ManyToManyField(Citation, blank=True)
	slaveOnly = models.NullBooleanField( default=False )
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
	
	def __unicode__(self):
		return self.name
	
	class MPTTMeta:
		order_insertion_by = ['name']

