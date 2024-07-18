from django.contrib import admin

from .models import WashingType, Booking


@admin.register(WashingType)
class WashingTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'number_of_places', 'price',)
    list_display_links = list_display
    list_filter = ('name', 'price',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('washing_type', 'week_days', 'arrival_time', 'full_name', 'phone_number', 'create_at',)
    list_display_links = list_display
    list_filter = ("washing_type", "week_days", "full_name", "phone_number",)

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True
