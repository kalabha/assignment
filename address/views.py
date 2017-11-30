from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from address.models import Coordinate
from geoposition import Geoposition

# Create your views here.
def get_address(request, get_latitude, get_longitude):
    try:
        location = Coordinate.objects.get(values=Geoposition(get_latitude, get_longitude))
    except ObjectDoesNotExist:
        geolocator = Nominatim()
        location = geolocator.reverse((get_latitude, get_longitude))
        Coordinate.objects.create(values=Geoposition(get_latitude, get_longitude), address=location.address)

    success = {"name": location.address}

    return JsonResponse(success, safe=False)
