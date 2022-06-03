from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrAdmin
from rest_framework.throttling import AnonRateThrottle


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []
