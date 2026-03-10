from rest_framework import serializers
from .models import Triage, AIanalyses

class TriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triage
        fields = '__all__'

class AIanalysesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIanalyses
        fields = '__all__'