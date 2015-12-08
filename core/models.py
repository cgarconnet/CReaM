# coding: utf8
from __future__ import unicode_literals # pour l'encoding facon Python 3
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from geoposition.fields import GeopositionField # adding maps to backends

import os
import uuid

# Create your models here.

EVENT_KIND = (
	(0, 'Facebook'),
	(1, 'Twitter'),
	(2, 'Instagram'),
	(3, 'Email'),
	(4, 'Soirée'),
	(5, 'Téléphone'),
	(6, 'RDV'),
	)


CUSTOMER_STATUS = (
	(0, 'Prospect - New'),
	(1, 'Prospect - Cold'),
	(2, 'Prospect - Hot'),
	(3, 'Active'),
	(4, 'Active - cold'),
	(5, 'Active - Hot'),
	)


CUSTOMER_KIND = (
	(0, 'Customer'),
	(1, 'Dealer'),
	(2, 'Host'),
	)

# Fonction from Django teacher to upload on Amazon with a new random name
# def upload_to_location(instance, filename):
#     blocks = filename.split('.')
#     ext = blocks[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     instance.title = blocks[0]
#     return os.path.join('uploads/', filename)

class Business(models.Model):
# il appartient à un user
	user = models.ForeignKey(User)
 	name = models.CharField(max_length=100, null=True, blank=True)

 	def __unicode__(self):
 		# return str(self.user) + ' / ' + str(self.name)
 		return self.name

 	def create_event_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="event_create", args=[self.id])

 	def create_customer_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="customer_create", args=[self.id])

 	def list_customer_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="customer_list", args=[self.id])
 
 	def list_event_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="business_event_list", args=[self.id])
 
  	def get_absolute_url(self):
 	# 	# return "location/"+str(self.id)+"/detail" # not the best way to do it
 	# 	# instead use the core.urlresolvers
 	 	return reverse (viewname="business_list")


class Customer(models.Model):
	user = models.ForeignKey(User)
	business = models.ForeignKey(Business) # could we make it multiple values

	kind = models.IntegerField(choices=CUSTOMER_KIND, null=True, blank=True)
	status = models.IntegerField(choices=CUSTOMER_STATUS, null=True, blank=True)

	fullname = models.CharField(max_length=100, null=True, blank=True)
	telephone = models.CharField(max_length=20, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)

	# position = GeopositionField(null=True, blank=True)

 	# image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

 	created_at = models.DateTimeField(auto_now_add=True)


 	# Code below allow us to define the title of the object in the Admin section
 	def __unicode__(self):
 		return self.fullname #+ ' - ' + str(self.bus_c) + ' - ' + str(self.fullname)
 		
 	def get_absolute_url(self):
 	 	return reverse (viewname="customer_list", args=[self.id])

 # 	def get_average_rating(self):
 # 		# django create a review_set if you have a Review class
 # 			average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
 # 			if average == None:
 # 				return average
	# 		else:
	# 			return int(average)


class Partner(models.Model):
	up = models.ForeignKey('self',related_name='up_level', null=True, blank=True) # could we make it multiple values
	left = models.ForeignKey('self',related_name='left_level', null=True, blank=True)
	right = models.ForeignKey('self',related_name='right_level', null=True, blank=True)
	value = models.CharField(max_length=100, null=True, blank=True)
	points = models.IntegerField(null=True, blank=True)

 	created_at = models.DateTimeField(auto_now_add=True)

 	def __unicode__(self):
 		return self.value #+ ' - ' + str(self.bus_c) + ' - ' + str(self.fullname)

 	def get_absolute_url(self):
 		return reverse (viewname="partner_detail", args=[self.id])


class Event(models.Model):
# il appartient à un client d'un user pour un Business
	user = models.ForeignKey(User)
	customer = models.ForeignKey(Customer)
	business = models.ForeignKey(Business)

	kind = models.IntegerField(choices=EVENT_KIND, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
 
  	# def __unicode__(self):
 		# return str(self.user) + ' / ' + self.created_at.strftime("%B %d, %Y") + ' / ' + str(self.rating)

 	# def __init__(self, *args, **kwargs):
		# super(EventCreateView, self).__init__(self, *args, **kwargs)
		# self.fields['bus_e'].queryset = Business.objects.filter(user=self.request.user)

 	def get_absolute_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="business_list")

    