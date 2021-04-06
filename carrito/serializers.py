
# Django REST Framework
from rest_framework import serializers
# Model
from autos.models import Autos

class AutosModelSerializer(serializers.ModelSerializer):
    """Education Model Serializer"""

    class Meta:
        """Meta class."""

        model = Autos
        fields = (
            'pk',
            'pk',
            'pk',
            'date_ini',
            'date_end',
            'title',
        )

class AutosSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    marca = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tipo = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField(required=False)
    title = serializers.CharField(max_length=255)

    def create(self, data):

        auto = Autos.objects.create(**data)
        return auto