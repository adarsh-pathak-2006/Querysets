from rest_framework.serializers import ModelSerializer
from .models import movies

class movie_serializer(ModelSerializer):
    class Meta:
        model=movies
        fields=['name', 'description']