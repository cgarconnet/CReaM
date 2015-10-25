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
import core.forms as forms # we import our models

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

class EventCreateView(CreateView):
	form_class = forms.EventCreateForm
#	model = coremodels.Event # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# # fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	# fields = ['customer', 'bus_e', 'type_e', 'description']

	# def get_form(self, request, obj=None, **kwargs):
	# 	form = super(EventCreateView, self).get_form(request, obj, **kwargs)
	# 	form.current_user = self.request.user
	# 	return form

	def get_form_kwargs(self):
		kwargs = super(EventCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs


#  	def __init__(self, **kwargs):
# 		super(EventCreateView, self).__init__(self, *kwargs)
# 		self.fields['bus_e'].queryset = coremodels.Business.objects.filter(user=self.request.user)
# http://stackoverflow.com/questions/24041649/filtering-a-model-in-a-createview-with-get-queryset

	# def get_queryset(self):
	# 	# return the review object for the current user and the current location
	# 	return coremodels.Event.objects.filter(user=self.request.user)

	def form_valid(self, form):
	# this feature is used between submission of the user and sending these data to the database
		form.instance.user = self.request.user
		return super(EventCreateView, self).form_valid(form)

# following line in error
	# def get_success_url(self): # returning the url of what we just edited
	# 	return self.object.Event.get_absolute_url()


# code for site authentification
# only specific here is the name of entrance page
@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
	return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})