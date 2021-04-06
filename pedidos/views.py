
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Serializers
from tipo.serializers import (TipoModelSerializer, TipoSerializer)

# Models
from tipo.models import Tipo

class TipoViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = TipoModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]


    def get_queryset(self):
        """Restrict list to only user Tipo formation."""
        queryset = Tipo.objects.filter(user=self.request.user)
        return queryset

        
    def create(self, request, *args, **kwargs):
        serializer = TipoSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = TipoModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
    