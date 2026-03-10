from rest_framework import viewsets
from .serializers import AIanalysesSerializer, TriageSerializer
from .models import AIanalyses, Triage
from .services.ai_service import GeminiService
from .services.maps_service import MapsService
from rest_framework.views import APIView
from rest_framework.response import Response

class TriageViewSet(viewsets.ModelViewSet):
    queryset = Triage.objects.all()
    serializer_class = TriageSerializer
    http_method_names = ['post','get'] # GET Temporary
 
    def perform_create(self, serializer):
 
        triage = serializer.save()
 
        service = GeminiService()
 
        resposta = service.analise(triage)
 
        AIanalyses.objects.create(
        triage=triage,
        prompt="triagem médica",
        resposta=resposta,
        model="gemini-3-flash-preview"
        )
        

class NearbyHospitalsView(APIView):
 
    def get(self, request):
    
        symptoms = request.get("symptoms")
        lat = request.data.get("lat")
        lng = request.data.get("lng")

        ai_service = GeminiService()
        ai_response = ai_service.analise(symptoms)
        speciality = ai_response["especialidades_recomendadas"][0]
        service = MapsService()
    
        hospitals = service.search_hospital(lat,lng,speciality)
    
        return Response(hospitals)

#class for tests !!!
# class NearbyHospitalsView(APIView):
 
#  def get(self, request):
 
#  lat = -23.3169879
#  lng = -46.7303273
#  speciality = 'Clinica Geral'
#  service = MapsService()
 
#  hospitals = service.search_hospital(lat,lng,speciality)
 
#  return Response(hospitals)


class AiAnalysesViewSet(viewsets.ModelViewSet):
    queryset = AIanalyses.objects.all()
    serializer_class = AIanalysesSerializer
    http_method_names = ['get']