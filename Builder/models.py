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
	
	class MPTTMeta:
		order_insertion_by = ['name']


class Clause(models.Model):
	node = models.ForeignKey(Node)
	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Family(models.Model):
	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Agreement(models.Model):
	filePath = models.FilePathField()
	node = models.OneToOneField(Node)
	families = models.ManyToManyField(Family)
	name = models.CharField(max_length=80, db_index = True)

	def __unicode__(self):
		return self.name


class ClauseProbability(models.Model):
	sigma = models.IntegerField()
	owner = models.OneToOneField(Clause, related_name = '+')
	relatives = models.ForeignKey(Clause)


