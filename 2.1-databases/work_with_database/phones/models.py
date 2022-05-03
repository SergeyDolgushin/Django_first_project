from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=30)
