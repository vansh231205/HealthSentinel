from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-symptom/', views.submit_symptom_report, name='submit_symptom'),
    path('api/water-quality/', views.get_water_quality_data, name='water_quality'),
    path('api/telemedicine/request/', views.request_telemedicine, name='request_telemedicine'),
    path('api/outbreak-alerts/', views.get_outbreak_alerts, name='outbreak_alerts'),
    path('api/community-report/', views.submit_community_report, name='community_report'),
    path('api/ai-assistant/', views.ai_voice_assistant, name='ai_assistant'),
    path('api/health-education/', views.get_health_education_modules, name='health_education'),
]