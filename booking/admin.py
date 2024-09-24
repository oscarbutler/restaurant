from django.contrib import admin
from .models import BookingSystem, Reviews

@admin.register(BookingSystem)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name','date', 'time', 'number_of_people']
    list_filter = ['date', 'time']
    search_fields = ['name', 'phone_number', 'email', 'date']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):