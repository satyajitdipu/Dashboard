# dashboard/serializers.py

from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'  # Use '__all__' or specify the fields you want to include/exclude
