from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='Датчик')
    description = models.CharField(
        max_length=40, verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    ids = models.ForeignKey(
        Sensor, related_name='Measurement', on_delete=models.CASCADE, verbose_name='ID датчика')
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
