# coding: utf8
from __future__ import unicode_literals # pour l'encoding facon Python 3
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

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
	paginate_by = 4 # definition of max py page

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Event.objects.filter(user=self.request.user).order_by('-created_at')


class BusinessEventListView(ListView):
	# this is a template view that will show list
	model = coremodels.Event
	template_name = "event/list.html"
	context_object_name = 'event'
	paginate_by = 4 # definition of max py page

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Event.objects.filter(user=self.request.user, business=self.kwargs['pk']).order_by('-created_at')


class BusinessCreateView(CreateView):
	model = coremodels.Business
#	model = coremodels.Event # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# # fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	fields = ['name']

	def form_valid(self, form):
	# this feature is used between submission of the user and sending these data to the database
		form.instance.user = self.request.user
		return super(BusinessCreateView, self).form_valid(form)


class EventDetailView(DetailView):
	# this is a template view that will show list
	model = coremodels.Event
	template_name = "event/detail.html"
	context_object_name = 'event'


class PartnerDetailView(DetailView):
	# this is a template view that will show list
	model = coremodels.Partner
	template_name = "partner/detail.html"
	context_object_name = 'partner'


class EventCreateView(CreateView):
	form_class = forms.EventCreateForm
#	model = coremodels.Event # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# # fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	# fields = ['customer', 'bus_e', 'type_e', 'description']


	def get_form_kwargs(self):
		kwargs = super(EventCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		kwargs['current_business'] = self.kwargs['pk']
		return kwargs


	def form_valid(self, form):
	# this feature is used between submission of the user and sending these data to the database
		form.instance.user = self.request.user
		form.instance.business = coremodels.Business.objects.get(id=self.kwargs['pk'])
		return super(EventCreateView, self).form_valid(form)


class CustomerListView(ListView):
	# this is a template view that will show list
	model = coremodels.Customer
	template_name = "customer/list.html"
#	context_object_name = 'business'

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Customer.objects.filter(user=self.request.user,business=self.kwargs['pk'])


class CustomerCreateView(CreateView):
#	form_class = forms.EventCreateForm2
	model = coremodels.Customer # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# # fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	fields = ['kind', 'status', 'fullname', 'telephone', 'email']
	context_object_name = 'customer'

	# def get_form_kwargs(self):
	# 	kwargs = super(CustomerCreateView, self).get_form_kwargs()
	# 	kwargs['user'] = self.request.user
	# 	kwargs['current_business'] = self.kwargs['pk']
	# 	return kwargs


	def form_valid(self, form):
	# this feature is used between submission of the user and sending these data to the database
		form.instance.user = self.request.user
		form.instance.business = coremodels.Business.objects.get(id=self.kwargs['pk'])
		return super(CustomerCreateView, self).form_valid(form)

	# def get_success_url(self): # returning the url of what we just edited
	# 	return self.object.customer.get_absolute_url()


class BusinessListView(ListView):
	# this is a template view that will show list
	model = coremodels.Business
	template_name = "business/list.html"
#	context_object_name = 'business'

	def get_queryset(self):
		# return the review object for the current user and the current location
		return coremodels.Business.objects.filter(user=self.request.user)

@csrf_exempt
def PartnerAddPoints(request, pk):
	# source: http://stackoverflow.com/questions/25135155/how-to-change-model-variable-by-onclick-function-used-in-template-asynchronously?answertab=active#tab-top
    value=request.POST.get("points")
    b=coremodels.Partner.objects.get(id=pk) #str(value))
    #delete change statement
    b.points = b.points + 10
    b.save()
    # resp=json.dumps(b)
#    return HttpResponse(resp, content_type="application/json")
	# I should now refresh the value in the DOM
    return HttpResponse(None, content_type="application/json")

# code for site authentification
# only specific here is the name of entrance page
@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
	return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})