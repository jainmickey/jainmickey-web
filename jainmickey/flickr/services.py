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
    cache_key = 'flickr_stream'
    stream_data = cache.get(cache_key)
    if not stream_data:
        stream_data = json.loads(flickr.photosets.getPhotos(photoset_id=settings.FLICKR_PHOTO_SET_ID,
                                                            extras='url_k,url_h,url_o,url_m,owner_name,'
                                                                   'views,date_upload').decode("utf-8"))
        cache.set(cache_key, stream_data, 172800)  # 2 day expiry
    return stream_data


def get_photo_from_flickr(photo_id):
    """
    Return a photo detail json fetched from flickr api.
    :photo_id
    """
    cache_key = 'flickr_{photo_id}'.format(photo_id)
    data = cache.get(cache_key)
    if not data:
        data = json.loads(flickr.photos.getInfo(photo_id=photo_id).decode("utf-8"))
        cache.set(cache_key, data, 604800)  # week expiry
    return data
