from rest_framework import serializers
from .models import AccAdvances

class AccAdvancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccAdvances
        fields = '__all__'
