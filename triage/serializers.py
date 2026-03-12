from rest_framework import serializers
from .models import Triage, AIanalyses

class TriageSerializer(serializers.ModelSerializer):
    """
    
    Serializer for medical triage data.

    Fields:
    - age: Patient age
    - symptom1: Primary symptom
    - symptom2: Secondary symptom
    - symptom3: Additional symptom
    - description: Additional details about the symptoms
    - duration: Duration of symptoms in days

    Example request body:

    {
      "age": 30,
      "symptom1": "fever",
      "symptom2": "chest pain",
      "symptom3": "cough",
      "description": "pain when breathing"
      "duration": 2,
    }
    
    """
    class Meta:
        model = Triage
        fields = '__all__'

class AIanalysesSerializer(serializers.ModelSerializer):
    """
    Serializer for AI-generated medical analyses.

    Fields:
    - triage: ID of the related triage
    - prompt: Prompt sent to the AI model
    - resposta: AI-generated analysis text
    - model: AI model used to generate the response

    """
    class Meta:
        model = AIanalyses
        fields = '__all__'