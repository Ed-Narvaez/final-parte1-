
# Django REST Framework
from rest_framework import serializers
# Model
from marca.models import Marca

class MarcaModelSerializer(serializers.ModelSerializer):
    """Marcas Model Serializer"""

    class Meta:
        """Meta class."""

        model = Marca
        fields = (
            'pk',
            'title',
            'description',
        )

class MarcaSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        marca = Marca.objects.create(**data)
        return Marca