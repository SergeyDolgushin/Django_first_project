from rest_framework.permissions import BasePermission
from sqlalchemy import true


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.creator_id == request.user.id or request.user.is_staff
