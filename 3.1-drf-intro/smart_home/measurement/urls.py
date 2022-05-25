from django.urls import path
from measurement.views import MeasurementView, SensorDetailView, SensorsViewCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
