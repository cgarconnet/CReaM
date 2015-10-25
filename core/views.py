from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render
from django.views.generic.base import TemplateView # to import html templates
from django.views.generic.list import ListView # to list my object from database
from django.views.generic.detail import DetailView # to show details of my selected object from database
from django.views.generic.edit import CreateView, UpdateView # to enable the edit form (create and then edit)

from sitegate.decorators import redirect_signedin, sitegate_view # for sitegate and authenficiation


import core.models as coremodels # we import our models
	
# Create your views here.

class LandingView(TemplateView):
		template_name = "base/theme.html"


class EventListView(ListView):
	# this is a template view that will show list
	model = coremodels.Event
	template_name = "event/list.html"
	context_object_name = 'event'

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Event.objects.filter(user=self.request.user)


class EventDetailView(DetailView):
	# this is a template view that will show list
		model = coremodels.Event
		template_name = "event/detail.html"
		context_object_name = 'event'

# code for site authentification
# only specific here is the name of entrance page
@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
	return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})