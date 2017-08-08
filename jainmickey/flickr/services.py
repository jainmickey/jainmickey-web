# Standard Library
import json
import logging

# Third Party Stuff
import flickrapi
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)
flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY, settings.FLICKR_SECRET_KEY, format='json', cache=True)


def get_photo_stream_from_flickr():
    """
    Return a photo stream json fetched from flickr api.
    """
    return json.loads(flickr.photosets.getPhotos(photoset_id=settings.FLICKR_PHOTO_SET_ID,
                                                 extras='url_k,url_h,url_o,url_m,owner_name,views,date_upload').decode("utf-8"))


def get_photo_from_flickr(photo_id):
    """
    Return a photo detail json fetched from flickr api.
    :photo_id
    """
    return json.loads(flickr.photos.getInfo(photo_id=photo_id).decode("utf-8"))
