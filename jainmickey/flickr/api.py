# Third Party Stuff
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from jainmickey.base import response

from . import services


class FlickrPhotoListAPIView(APIView):
    """
    API endpoint that fetch the flickr photo stream.
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        data = services.get_photo_stream_from_flickr()
        if not data:
            return response.BadRequest({'message': 'Error in fetching data from flickr api.'})
        return response.Ok(data)


class FlickrPhotoDetailAPIView(APIView):
    """
    API endpoint that fetch the flickr photo stream.
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        photo_id = request.query_params.get('photo_id', None)
        data = services.get_photo_from_flickr(photo_id)
        if not data:
            return response.BadRequest({'message': 'Error in fetching data from flickr api.'})
        return response.Ok(data)
