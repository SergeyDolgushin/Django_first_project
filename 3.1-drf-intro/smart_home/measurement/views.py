# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, SensorPatchSerializer


class SensorsViewCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self, ):
        if self.request.method == 'GET':
            return SensorDetailSerializer

        return SensorPatchSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# class MeasurementView(APIView):
#     def post(self, request):
#         measurement = request.data

#         serializer = MeasurementSerializer(
#             data=measurement)
#         if serializer.is_valid(raise_exception=True):
#             data_saved = serializer.save()
#         return Response({"success": "New data added successfully"})

# class SensorsView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)

#     def post(self, request):
#         new_sensor = request.data
#         serializer = SensorSerializer(data=new_sensor)
#         if serializer.is_valid(raise_exception=True):
#             data_saved = serializer.save()
#         return Response({"success": "New sensor added successfully"})
