from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime, timedelta
import random
import hashlib

# Simulated API endpoints for the HealthSentinel prototype

@csrf_exempt
@require_http_methods(["POST"])
def submit_symptom_report(request):
    """Submit symptom report and get AI analysis"""
    try:
        data = json.loads(request.body)
        symptoms = data.get('symptoms', '')
        location = data.get('location', '')
        voice_transcript = data.get('voice_transcript', '')
        
        # Simulate AI analysis
        risk_level = analyze_symptoms(symptoms + ' ' + voice_transcript)
        predicted_disease = predict_disease(symptoms + ' ' + voice_transcript)
        
        # Simulate saving to database
        report_id = random.randint(1000, 9999)
        
        response = {
            'success': True,
            'report_id': report_id,
            'ai_analysis': {
                'risk_level': risk_level,
                'predicted_disease': predicted_disease,
                'recommendations': get_recommendations(risk_level, predicted_disease),
                'should_contact_doctor': risk_level in ['HIGH', 'CRITICAL']
            },
            'message': 'Report submitted successfully. Health authorities have been notified if necessary.'
        }
        
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def get_water_quality_data(request):
    """Get current water quality data from sensors"""
    # Simulate IoT sensor data
    sensors = [
        {
            'sensor_id': 'WS001',
            'location': 'Village A Well',
            'ph': round(random.uniform(6.0, 8.5), 1),
            'tds': random.randint(50, 500),
            'turbidity': round(random.uniform(0.1, 5.0), 1),
            'bacterial_count': random.randint(0, 100),
            'latitude': 25.3176,
            'longitude': 82.9739,
            'timestamp': datetime.now().isoformat(),
            'is_safe': True
        },
        {
            'sensor_id': 'WS002',
            'location': 'Village B Pond',
            'ph': round(random.uniform(5.5, 9.0), 1),
            'tds': random.randint(100, 800),
            'turbidity': round(random.uniform(1.0, 10.0), 1),
            'bacterial_count': random.randint(0, 200),
            'latitude': 25.3200,
            'longitude': 82.9800,
            'timestamp': datetime.now().isoformat(),
            'is_safe': True
        }
    ]
    
    # Determine safety based on parameters
    for sensor in sensors:
        if (sensor['ph'] < 6.5 or sensor['ph'] > 8.5 or 
            sensor['tds'] > 500 or sensor['bacterial_count'] > 50):
            sensor['is_safe'] = False
    
    return JsonResponse({'sensors': sensors})

@csrf_exempt
@require_http_methods(["POST"])
def request_telemedicine(request):
    """Request telemedicine consultation"""
    try:
        data = json.loads(request.body)
        patient_name = data.get('patient_name', '')
        symptoms = data.get('symptoms', '')
        urgency = data.get('urgency', 'normal')
        
        # Simulate doctor assignment
        doctors = ['Dr. Sharma', 'Dr. Patel', 'Dr. Singh', 'Dr. Kumar']
        assigned_doctor = random.choice(doctors)
        
        # Simulate session ID
        session_id = hashlib.md5(f"{patient_name}{datetime.now()}".encode()).hexdigest()[:8]
        
        # Calculate wait time based on urgency
        wait_time = 5 if urgency == 'urgent' else 15
        
        response = {
            'success': True,
            'session_id': session_id,
            'assigned_doctor': assigned_doctor,
            'estimated_wait_time': wait_time,
            'meeting_link': f"https://meet.healthsentinel.com/{session_id}",
            'message': f'Consultation scheduled with {assigned_doctor}. You will be contacted in {wait_time} minutes.'
        }
        
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def get_outbreak_alerts(request):
    """Get current outbreak alerts"""
    alerts = [
        {
            'id': 1,
            'disease_type': 'Cholera',
            'location': 'Zone A',
            'alert_level': 'WARNING',
            'affected_population': 45,
            'description': 'Increased cholera cases detected. Water sources under investigation.',
            'recommendations': 'Boil water before consumption. Maintain hygiene.',
            'created_at': (datetime.now() - timedelta(hours=2)).isoformat(),
            'is_active': True
        },
        {
            'id': 2,
            'disease_type': 'Diarrhea',
            'location': 'Village B',
            'alert_level': 'WATCH',
            'affected_population': 12,
            'description': 'Multiple diarrhea cases reported. Monitoring situation.',
            'recommendations': 'Stay hydrated. Seek medical attention if symptoms worsen.',
            'created_at': (datetime.now() - timedelta(hours=6)).isoformat(),
            'is_active': True
        }
    ]
    
    return JsonResponse({'alerts': alerts})

@csrf_exempt
@require_http_methods(["POST"])
def submit_community_report(request):
    """Submit community health report"""
    try:
        data = json.loads(request.body)
        reporter = data.get('reporter', 'Anonymous')
        report_type = data.get('report_type', 'HEALTH')
        issue = data.get('issue', '')
        location = data.get('location', '')
        
        report_id = random.randint(10000, 99999)
        
        response = {
            'success': True,
            'report_id': report_id,
            'message': 'Community report submitted successfully. Thank you for helping keep our community safe!',
            'verification_status': 'PENDING'
        }
        
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def ai_voice_assistant(request):
    """AI voice assistant endpoint"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()
        
        # Simple AI response logic
        response_text = process_voice_command(user_message)
        
        return JsonResponse({
            'success': True,
            'response': response_text,
            'action': determine_action(user_message)
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def get_health_education_modules(request):
    """Get available health education modules"""
    modules = [
        {
            'id': 1,
            'title': 'Water Hygiene Basics',
            'description': 'Learn about safe water practices',
            'points': 100,
            'difficulty': 'Easy',
            'duration': '10 minutes',
            'completed': False
        },
        {
            'id': 2,
            'title': 'Disease Prevention',
            'description': 'How to prevent water-borne diseases',
            'points': 150,
            'difficulty': 'Medium',
            'duration': '15 minutes',
            'completed': False
        },
        {
            'id': 3,
            'title': 'First Aid Basics',
            'description': 'Basic first aid for common illnesses',
            'points': 200,
            'difficulty': 'Hard',
            'duration': '20 minutes',
            'completed': False
        }
    ]
    
    return JsonResponse({'modules': modules})

# Helper functions
def analyze_symptoms(symptoms):
    """Simulate AI symptom analysis"""
    symptoms_lower = symptoms.lower()
    
    high_risk_keywords = ['blood', 'severe', 'fever high', 'vomiting', 'dehydration']
    medium_risk_keywords = ['diarrhea', 'fever', 'nausea', 'stomach pain', 'headache']
    
    if any(keyword in symptoms_lower for keyword in high_risk_keywords):
        return 'HIGH'
    elif any(keyword in symptoms_lower for keyword in medium_risk_keywords):
        return 'MEDIUM'
    else:
        return 'LOW'

def predict_disease(symptoms):
    """Simulate AI disease prediction"""
    symptoms_lower = symptoms.lower()
    
    if 'diarrhea' in symptoms_lower and 'fever' in symptoms_lower:
        return 'Cholera (suspected)'
    elif 'stomach pain' in symptoms_lower and 'fever' in symptoms_lower:
        return 'Typhoid (suspected)'
    elif 'diarrhea' in symptoms_lower:
        return 'Gastroenteritis (suspected)'
    elif 'fever' in symptoms_lower:
        return 'Viral infection (suspected)'
    else:
        return 'General illness (suspected)'

def get_recommendations(risk_level, disease):
    """Get medical recommendations based on analysis"""
    if risk_level == 'HIGH':
        return 'Seek immediate medical attention. Stay hydrated. Avoid solid foods.'
    elif risk_level == 'MEDIUM':
        return 'Monitor symptoms closely. Stay hydrated. Rest. Contact healthcare provider if symptoms worsen.'
    else:
        return 'Rest and stay hydrated. Monitor symptoms. Contact healthcare provider if symptoms persist.'

def process_voice_command(message):
    """Process voice commands and return appropriate response"""
    if 'call doctor' in message or 'doctor' in message:
        return "I'll help you connect with a doctor. Please wait while I find an available healthcare provider."
    elif 'water quality' in message:
        return "Let me check the latest water quality data for your area."
    elif 'symptoms' in message or 'feeling sick' in message:
        return "I can help you report your symptoms. Please describe how you're feeling."
    elif 'emergency' in message or 'help' in message:
        return "This seems urgent. I'm connecting you to emergency services and the nearest health worker."
    elif 'education' in message or 'learn' in message:
        return "I can help you learn about health and hygiene. Let me show you some interactive lessons."
    else:
        return "I'm here to help with your health needs. You can ask me about symptoms, water quality, calling a doctor, or health education."

def determine_action(message):
    """Determine what action to take based on voice command"""
    if 'call doctor' in message:
        return 'open_telemedicine'
    elif 'water quality' in message:
        return 'show_water_data'
    elif 'symptoms' in message:
        return 'open_symptom_report'
    elif 'emergency' in message:
        return 'emergency_call'
    elif 'education' in message:
        return 'open_education'
    else:
        return 'none'