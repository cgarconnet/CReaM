from django.forms import ModelForm

import core.models as coremodels # we import our models


class EventCreateForm2(ModelForm):

	class Meta:
		model = coremodels.Event
		fields = ['customer', 'kind', 'description']

	def __init__(self, current_business, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		current_user = kwargs.pop('user')
#		current_business = kwargs['pk']
		super(EventCreateForm2, self).__init__(*args, **kwargs)
		#self.fields['customer'].queryset = 
		self.fields['customer'].queryset = coremodels.Customer.objects.filter(user=current_user,business=current_business)
#		self.fields['customer'].queryset = coremodels.Customer.objects.filter(user=current_user)
#		self.fields['business'].queryset = coremodels.Business.objects.filter(user=current_user)

