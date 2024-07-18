from django.urls import path

from bookings.views import BookingListCreateAPIView, WashingTypeListAPIView
urlpatterns = [
    path('', BookingListCreateAPIView.as_view(), name='bookings'),
    path('washing_type/', WashingTypeListAPIView.as_view(), name='washing_type')
]