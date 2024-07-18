from rest_framework import generics

from bookings.models import Booking, WashingType
from bookings.serializers import BookingSerializer, WashingTypeSerializer


class WashingTypeListAPIView(generics.ListAPIView):
    queryset = WashingType.objects.all()
    serializer_class = WashingTypeSerializer


class BookingListCreateAPIView(generics.CreateAPIView):
    model = Booking
    serializer_class = BookingSerializer
