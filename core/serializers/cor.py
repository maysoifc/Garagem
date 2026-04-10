from rest_framework.serializers import ModelSerializer
from core.models import core

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'