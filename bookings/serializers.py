from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bookings.models import Booking, WashingType


class WashingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashingType
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        arrival_datetime = datetime.combine(datetime.today(), data['arrival_time'])
        end_time = arrival_datetime + timedelta(minutes=data['washing_type'].time)

        objs = Booking.objects.filter(
            week_days=data['week_days'],
            washing_type=data['washing_type'],
            arrival_time__range=(data['arrival_time'], end_time.time())
        )

        if objs.count() >= data['washing_type'].number_of_places:
            raise ValidationError("This time is already booked")
        return super().validate(data)
