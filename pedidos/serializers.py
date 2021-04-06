
# Django REST Framework
from rest_framework import serializers
# Model
from tipo.models import Tipo

class TipoModelSerializer(serializers.ModelSerializer):
    """Extras Model Serializer"""

    class Meta:
        """Meta class."""

        model = Tipo
        fields = (
            'pk',
            'title',
            'description',
        )

class TipoSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        tipo = Tipo.objects.create(**data)
        return tipo