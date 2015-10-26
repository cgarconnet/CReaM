from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required # to block users who are not logged is so that cannot create
# all url that we want to protect we add login_required()

import core.views as coreviews


urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
	url(r'event/$', login_required(coreviews.EventListView.as_view())),
	url(r'event/create/$', login_required(coreviews.EventCreateView.as_view())),
	url(r'event/(?P<pk>\d+)/create/$', login_required(coreviews.EventCreateView2.as_view()), name = 'event_create'),
	url(r'event/(?P<pk>\d+)/detail/$', coreviews.EventDetailView.as_view(), name = 'event_list'),

	url(r'business/$', login_required(coreviews.BusinessListView.as_view())),

	url(r'customer/(?P<pk>\d+)/$', login_required(coreviews.CustomerListView.as_view()), name = 'customer_list'),
	url(r'customer/(?P<pk>\d+)/create/$', login_required(coreviews.CustomerCreateView.as_view()), name = 'customer_create'),

	# Registering the entrance login page
	url(r'entrance/$', coreviews.entrance),

	# easy url to logout
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/entrance'})
		# next page coulb be our /entrance

)
