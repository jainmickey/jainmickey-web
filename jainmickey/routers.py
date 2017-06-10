# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from django.conf.urls import url
from rest_framework import routers

from jainmickey.flickr.api import FlickrPhotoDetailAPIView, FlickrPhotoListAPIView

router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = router.urls + [
    url(r'^flickr/detail$', FlickrPhotoDetailAPIView.as_view(), name='flickr_detail'),
    url(r'^flickr$', FlickrPhotoListAPIView.as_view(), name='flickr_list'),
]
