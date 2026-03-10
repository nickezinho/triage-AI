from django.contrib import admin
from django.urls import path,include
from triage.views import NearbyHospitalsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('triage.urls')),
    path('hospitals/', NearbyHospitalsView.as_view())
]
