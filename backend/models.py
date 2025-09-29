from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import uuid

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    preferred_language = models.CharField(max_length=10, default='en-IN')
    is_health_worker = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class SymptomReport(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical')
    ]
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    symptoms = models.TextField()
    voice_transcript = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ai_risk_level = models.CharField(max_length=10, choices=RISK_LEVELS, default='LOW')
    ai_predicted_disease = models.CharField(max_length=100, blank=True)
    is_outbreak_potential = models.BooleanField(default=False)
    response_sent = models.BooleanField(default=False)

class WaterSensorData(models.Model):
    sensor_id = models.CharField(max_length=50)
    ph = models.FloatField()
    tds = models.FloatField()
    turbidity = models.FloatField()
    bacterial_count = models.IntegerField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_safe = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommunityReport(models.Model):
    REPORT_TYPES = [
        ('HEALTH', 'Health Issue'),
        ('WATER', 'Water Quality'),
        ('SANITATION', 'Sanitation Problem'),
        ('OUTBREAK', 'Disease Outbreak')
    ]
    
    reporter = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    issue = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image_url = models.URLField(blank=True)
    verification_status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

class OutbreakAlert(models.Model):
    ALERT_LEVELS = [
        ('WATCH', 'Watch'),
        ('WARNING', 'Warning'),
        ('EMERGENCY', 'Emergency')
    ]
    
    disease_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    alert_level = models.CharField(max_length=10, choices=ALERT_LEVELS)
    affected_population = models.IntegerField()
    description = models.TextField()
    recommendations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class HealthEducationProgress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    module_completed = models.CharField(max_length=100)
    score = models.IntegerField()
    points_earned = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

class TelemedicineSession(models.Model):
    SESSION_STATUSES = [
        ('REQUESTED', 'Requested'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    session_id = models.UUIDField(default=uuid.uuid4)
    status = models.CharField(max_length=20, choices=SESSION_STATUSES, default='REQUESTED')
    symptoms_reported = models.TextField()
    prescription = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()

class AIHealthRecord(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    record_hash = models.CharField(max_length=256)  # Blockchain hash
    health_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
