from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render
from django.views.generic.base import TemplateView # to import html templates
from django.views.generic.list import ListView # to list my object from database
from django.views.generic.detail import DetailView # to show details of my selected object from database
from django.views.generic.edit import CreateView, UpdateView # to enable the edit form (create and then edit)

import core.models as coremodels # we import our models
	
# Create your views here.

class LandingView(TemplateView):
		template_name = "base/index.html"


class EventListView(ListView):
	# this is a template view that will show list
	model = coremodels.Event
	template_name = "event/list.html"
	context_object_name = 'event'

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Event.objects.filter(user=self.request.user)

	# def get_context_data(self, **kwargs):
	# 	# the reverse as form_valid. Modify data between extract from DB -> page
	# 	context = super(EventListView, self).get_context_data(**kwargs)
	# 	# location = coremodels.Location.objects.get(id=self.kwargs['pk'])

	# 	if self.request.user.is_authenticated():
	# 		user_reviews = coremodels.Event.objects.filter(user=self.request.user)
	# 		# if user_reviews.count() > 0:
	# 		# 	context['user_review'] = user_reviews[0]
	# 		# else:
	# 		# 	context['user_review'] = None
	# 	return context

class EventDetailView(DetailView):
	# this is a template view that will show list
		model = coremodels.Event
		template_name = "event/detail.html"
		context_object_name = 'event'

