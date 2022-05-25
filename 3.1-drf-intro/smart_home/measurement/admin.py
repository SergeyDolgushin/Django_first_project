from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor)
class SnesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at']
