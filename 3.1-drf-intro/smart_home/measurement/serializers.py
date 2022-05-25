from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        return instance

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

    class Meta:
        model = Measurement
        fields = ['ids', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    Measurement = MeasurementSerializer(read_only=True, many=True)

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'Measurement']
