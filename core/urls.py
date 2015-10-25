from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required # to block users who are not logged is so that cannot create
# all url that we want to protect we add login_required()

import core.views as coreviews


urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
	url(r'event/$', login_required(coreviews.EventListView.as_view())),
	url(r'event/create/$', login_required(coreviews.EventCreateView.as_view())),

	url(r'event/(?P<pk>\d+)/detail/$', coreviews.EventDetailView.as_view(), name = 'event_list'),

	# Registering the entrance login page
	url(r'entrance/$', coreviews.entrance),

	# easy url to logout
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/entrance'})
		# next page coulb be our /entrance

)
