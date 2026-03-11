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

        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")
        speciality = request.query_params.get("speciality")

        service = MapsService()

        hospitals = service.search_hospital(lat, lng, speciality)

        return Response(hospitals)


# #class for tests !!!
# class NearbyHospitalsView(APIView):
 
#     def get(self, request):
 
#         lat = -23.3169879
#         lng = -46.7303273
#         speciality = 'Clinica Geral'
#         service = MapsService()
 
#         hospitals = service.search_hospital(lat,lng,speciality)
 
#         return Response(hospitals)


class AiAnalysesViewSet(viewsets.ModelViewSet):
    queryset = AIanalyses.objects.all()
    serializer_class = AIanalysesSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = AIanalyses.objects.all()
        triage_id = self.request.query_params.get('triage')

        if triage_id:
            queryset = queryset.filter(triage_id=triage_id)
        
        return queryset

