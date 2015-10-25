from django.conf.urls import patterns, include, url
# from django.contrib.auth.decorators import login_required # to block users who are not logged is so that cannot create
# all url that we want to protect we add login_required()

import core.views as coreviews

# urlpatterns = patterns('',

# 	# url(r'^$', coreviews.LandingView.as_view()),
# 	url(r'^$', coreviews.LandingView,

# )

urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
)
