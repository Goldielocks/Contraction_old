from django.db import models
from django import forms
from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
	name = models.CharField(max_length=80)
	def __unicode__(self):
			return self.name

class Node(MPTTModel):
	category = models.ForeignKey(Category)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name
	
#	class MPTTMeta:
#		order_insertion_by = ['name']


class Clause(models.Model):
	node = models.ForeignKey(Node)
	start = models.IntegerField()
	end = models.IntegerField()
	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Family(models.Model):
	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Contract(models.Model):
	filePath = models.CharField(max_length=200)
	node = models.OneToOneField(Node)
	families = models.ManyToManyField(Family)
	name = models.CharField(max_length=80, blank = True)

	def __unicode__(self):
		return self.name


class ClauseProbability(models.Model):
	sigma = models.DecimalField(decimal_places=6, max_digits=8)
	owner = models.OneToOneField(Clause, related_name = '+')
	relatives = models.ForeignKey(Clause)


