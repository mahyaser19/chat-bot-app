from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import re
import pandas as pd
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from data import intent_patterns, vehicle_problems, service_packages, service_pricing, maintenance_tips
from arabic_data import intent_patterns_ar, vehicle_problems_ar, service_pricing_ar, maintenance_tips_ar
from maintenance_data import maintenance_procedures, maintenance_procedures_ar, diagnostic_procedures, diagnostic_procedures_ar
from ai_handler import generate_ai_response, enhance_response

load_dotenv()

app = Flask(__name__)
CORS(app)

def is_arabic(text):
    # Check if the text contains Arabic characters
    arabic_pattern = re.compile('[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    return bool(arabic_pattern.search(text))

def detect_intent(user_input, patterns):
    user_input = user_input.lower()
    
    # First check for inappropriate language
    if 'inappropriate_language' in patterns:
        if any(pattern in user_input.lower() for pattern in patterns['inappropriate_language']['patterns']):
            return {'intent': 'inappropriate_language'}
    
    # Check for maintenance procedure requests
    maintenance_keywords = ['how to', 'steps', 'procedure', 'guide', 'instructions'] if not is_arabic(user_input) else ['كيف', 'خطوات', 'طريقة', 'دليل', 'تعليمات']
    for proc_type in maintenance_procedures.keys():
        if proc_type in user_input.lower() and any(keyword in user_input.lower() for keyword in maintenance_keywords):
            return {'intent': 'maintenance_procedure', 'procedure_type': proc_type}
    
    # Check for diagnostic requests
    diagnostic_keywords = ['diagnose', 'problem', 'issue', 'troubleshoot'] if not is_arabic(user_input) else ['تشخيص', 'مشكلة', 'عطل', 'حل']
    for prob_type in diagnostic_procedures.keys():
        if prob_type in user_input.lower() and any(keyword in user_input.lower() for keyword in diagnostic_keywords):
            return {'intent': 'diagnostic_info', 'problem_type': prob_type}
    
    # Check for other intents
    for intent, data in patterns.items():
        if intent != 'inappropriate_language' and any(pattern in user_input.lower() for pattern in data['patterns']):
            if intent == 'service_inquiry':
                if 'oil' in user_input or 'زيت' in user_input:
                    return {'intent': intent, 'sub_intent': 'oil_change'}
                elif 'tire' in user_input or 'إطار' in user_input or 'اطار' in user_input:
                    return {'intent': intent, 'sub_intent': 'tire_rotation'}
                elif 'brake' in user_input or 'فرامل' in user_input:
                    return {'intent': intent, 'sub_intent': 'brake_inspection'}
                return {'intent': intent, 'sub_intent': 'general'}
            elif intent == 'technical_issue':
                if 'noise' in user_input or 'صوت' in user_input:
                    return {'intent': intent, 'sub_intent': 'noise'}
                elif 'brake' in user_input or 'فرامل' in user_input:
                    return {'intent': intent, 'sub_intent': 'brake'}
                elif ('engine' in user_input and 'light' in user_input) or ('محرك' in user_input and 'لمبة' in user_input):
                    return {'intent': intent, 'sub_intent': 'engine_light'}
                return {'intent': intent, 'sub_intent': 'general'}
            elif intent == 'service_packages':
                if 'basic' in user_input or 'أساسي' in user_input or 'اساسي' in user_input:
                    return {'intent': intent, 'sub_intent': 'basic'}
                elif 'standard' in user_input or 'قياسي' in user_input:
                    return {'intent': intent, 'sub_intent': 'standard'}
                elif 'platinum' in user_input or 'بلاتيني' in user_input:
                    return {'intent': intent, 'sub_intent': 'platinum'}
                elif 'comprehensive' in user_input or 'شامل' in user_input:
                    return {'intent': intent, 'sub_intent': 'comprehensive'}
                return {'intent': intent, 'sub_intent': 'general'}
            return {'intent': intent}
    
    return {'intent': 'unknown'}

def get_vehicle_type_problems(vehicle_type, is_ar=False):
    problems = vehicle_problems_ar if is_ar else vehicle_problems
    if vehicle_type and vehicle_type.lower() in problems:
        car_type = problems[vehicle_type.lower()]
        response = f"{car_type['name']} - {'المشاكل الشائعة والحلول' if is_ar else 'Common Problems and Solutions'}:\n\n"
        for problem, solution in car_type['problems'].items():
            response += f"{'المشكلة' if is_ar else 'Problem'}: {problem}\n"
            response += f"{'الحل' if is_ar else 'Solution'}: {solution}\n\n"
        return response
    return None

def get_maintenance_tips(category=None, subcategory=None, is_ar=False):
    tips = maintenance_tips_ar if is_ar else maintenance_tips
    if not category:
        tip_list = tips['general']
        response = "نصائح الصيانة العامة:\n\n" if is_ar else "General Maintenance Tips:\n\n"
        for tip in tip_list:
            response += f"- {tip}\n"
        return response
    elif category in tips:
        if subcategory and subcategory in tips[category]:
            tip_list = tips[category][subcategory]
            response = f"{category.title()} - {subcategory.title()} {'نصائح الصيانة' if is_ar else 'Maintenance Tips'}:\n\n"
            for tip in tip_list:
                response += f"- {tip}\n"
            return response
    return None

def get_maintenance_procedure(procedure_type, is_ar=False):
    procedures = maintenance_procedures_ar if is_ar else maintenance_procedures
    if procedure_type and procedure_type.lower() in procedures:
        procedure = procedures[procedure_type.lower()]
        response = f"{procedure['name']}:\n\n"
        
        response += "خطوات العمل:\n" if is_ar else "Steps:\n"
        for i, step in enumerate(procedure['steps'], 1):
            response += f"{i}. {step}\n"
        
        response += "\nالأدوات المطلوبة:\n" if is_ar else "\nTools Needed:\n"
        for tool in procedure['tools_needed']:
            response += f"- {tool}\n"
        
        response += "\nملاحظات السلامة:\n" if is_ar else "\nSafety Notes:\n"
        for note in procedure['safety_notes']:
            response += f"- {note}\n"
            
        return response
    return None

def get_diagnostic_info(problem_type, is_ar=False):
    diagnostics = diagnostic_procedures_ar if is_ar else diagnostic_procedures
    if problem_type and problem_type.lower() in diagnostics:
        problem = diagnostics[problem_type.lower()]
        response = f"{'تشخيص المشكلة' if is_ar else 'Problem Diagnosis'}:\n\n"
        
        response += "الأعراض:\n" if is_ar else "Symptoms:\n"
        for symptom in problem['symptoms']:
            response += f"- {symptom}\n"
        
        response += "\nالأسباب المحتملة:\n" if is_ar else "\nPossible Causes:\n"
        for cause in problem['possible_causes']:
            response += f"- {cause}\n"
        
        response += "\nخطوات التشخيص:\n" if is_ar else "\nDiagnostic Steps:\n"
        for i, step in enumerate(problem['diagnostic_steps'], 1):
            response += f"{i}. {step}\n"
            
        return response
    return None

def get_response(user_input):
    # Detect language
    is_ar = is_arabic(user_input)
    patterns = intent_patterns_ar if is_ar else intent_patterns
    
    # First try to get a structured response
    intent_data = detect_intent(user_input, patterns)
    intent = intent_data['intent']
    base_response = None
    
    # Handle maintenance procedures
    if intent == 'maintenance_procedure':
        procedure_type = intent_data.get('procedure_type')
        base_response = get_maintenance_procedure(procedure_type, is_ar)
    
    # Handle diagnostic information
    elif intent == 'diagnostic_info':
        problem_type = intent_data.get('problem_type')
        base_response = get_diagnostic_info(problem_type, is_ar)
    
    # Get appropriate response based on intent
    elif intent in patterns:
        if isinstance(patterns[intent]['responses'], dict):
            sub_intent = intent_data.get('sub_intent', 'general')
            base_response = patterns[intent]['responses'][sub_intent]
        else:
            base_response = patterns[intent]['responses'][0]
    
    # If we have a structured response, enhance it with AI
    if base_response:
        try:
            return enhance_response(base_response, user_input, is_ar)
        except:
            return base_response
    
    # If no structured response found, generate AI response
    context = """
    This is a car service chatbot that can help with:
    1. Service packages and pricing
    2. Vehicle maintenance procedures
    3. Diagnostic information
    4. Scheduling appointments
    5. General automotive advice
    """
    
    return generate_ai_response(user_input, context, is_ar)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
