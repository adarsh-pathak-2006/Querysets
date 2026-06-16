from rest_framework.serializers import ModelSerializer
from .models import db

class db_serializer(ModelSerializer):
    class Meta:
        model=db
        fields='__all__'