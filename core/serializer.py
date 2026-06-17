from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import db,f1

class db_serializer(ModelSerializer):
    class Meta:
        model=db
        fields='__all__'


class f1_serializer(ModelSerializer):
    class Meta:
        model=f1
        fields=['driver', 'team']


