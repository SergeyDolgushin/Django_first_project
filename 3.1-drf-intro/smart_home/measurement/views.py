# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        new_sensor = request.data
        serializer = SensorSerializer(data=new_sensor)
        if serializer.is_valid(raise_exception=True):
            data_saved = serializer.save()
        return Response({"success": "New sensor added successfully"})


class SensorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(APIView):
    def post(self, request):
        measurement = request.data
        measurement['ids'] = measurement.pop('sensor')

        serializer = MeasurementSerializer(data=measurement)
        if serializer.is_valid(raise_exception=True):
            data_saved = serializer.save()
        return Response({"success": "New data added successfully"})
