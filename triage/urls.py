from rest_framework import routers
from .views import TriageViewSet, AiAnalysesViewSet

router = routers.DefaultRouter()

router.register('triage', TriageViewSet, basename='triage')
router.register('analyses', AiAnalysesViewSet, basename='analyses')

urlpatterns = router.urls