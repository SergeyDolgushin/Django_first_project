from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']
        extra_kwargs = {
            'sensor': {'write_only': True},
        }


class SensorDetailSerializer(serializers.ModelSerializer):
    Measurement = MeasurementSerializer(read_only=True, many=True)

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'Measurement']


class SensorPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
