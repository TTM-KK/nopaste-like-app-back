
from rest_framework.serializers import ModelSerializer
from .models import TextData


class TextSerializer(ModelSerializer):
    class Meta:
        model = TextData
        fields = ('text', 'id')
