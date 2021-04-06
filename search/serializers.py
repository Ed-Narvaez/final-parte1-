
# Django REST Framework
from rest_framework import serializers

# Models
from users.models import User
from experiences.models import Experience
from autos.models import Autos
from marca.models import Marca
from tipo.models import Tipo


class ExperienceSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experience
        fields = [
            'date_ini',
            'date_end',
            'company',
            'description',
        ]
class TipoSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Tipo
        fields = [
            'title',
            'description',
        ]
class MarcaSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Marca
        fields = [
            'title',
            'description',
        ]

class AutosSerializer(serializers.ModelSerializer):
    """Education Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Autos
        fields = (
            'date_ini',
            'date_end',
            'title',
        )