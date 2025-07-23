"""
Car Service Chatbot Dataset
Contains all structured data for the chatbot including intents, responses, 
service packages, vehicle problems, and pricing information.
"""

# Basic service pricing
service_pricing = {
    'oil_change': {'price': 600, 'duration': 30, 'currency': 'ج.م.'},
    'tire_rotation': {'price': 250, 'duration': 20, 'currency': 'ج.م.'},
    'brake_inspection': {'price': 400, 'duration': 20, 'currency': 'ج.م.'}
}

# Service packages data
service_packages = {
    'basic': {
        'name': 'Basic Service Package',
        'price': 2999,
        'currency': 'ج.م.',
        'interval': 'Every 5,000 km or 6 months',
        'services': [
            'Oil and filter change',
            'Tire pressure check and adjustment',
            'Basic safety inspection',
            'Fluid level check and top-up',
            'Battery check'
        ]
    },
    'standard': {
        'name': 'Standard Service Package',
        'price': 4999,
        'currency': 'ج.م.',
        'interval': 'Every 10,000 km or 12 months',
        'services': [
            'All Basic Package services',
            'Brake system inspection',
            'Air filter replacement',
            'Cabin filter check',
            'Wheel alignment check',
            'Belt and hose inspection'
        ]
    },
    'platinum': {
        'name': 'Platinum Service Package',
        'price': 7495,
        'currency': 'ج.م.',
        'interval': 'Every 20,000 km or 18 months',
        'services': [
            'All Standard Package services',
            'Transmission fluid check',
            'Spark plug replacement',
            'Thorough brake service',
            'AC system check',
            'Advanced computer diagnostics'
        ]
    },
    'comprehensive': {
        'name': 'Comprehensive Service Package',
        'price': 9495,
        'currency': 'ج.م.',
        'interval': 'Every 40,000 km or 24 months',
        'services': [
            'All Platinum Package services',
            'Major tune-up',
            'Transmission service',
            'Coolant system flush',
            'Fuel system cleaning',
            'Complete vehicle inspection'
        ]
    }
}

# Vehicle problems database
vehicle_problems = {
    'ice': {
        'name': 'Internal Combustion Engine Cars',
        'problems': {
            'Engine overheating': 'Check coolant levels, radiator condition, and thermostat functionality. May require professional inspection.',
            'Transmission issues': 'Check transmission fluid, look for leaks. May need professional diagnosis for internal problems.',
            'Exhaust smoke': 'Different colored smoke indicates different issues: blue (oil burning), white (coolant leak), black (rich fuel mixture).',
            'Poor fuel economy': 'Check tire pressure, air filters, and driving habits. May require tune-up or oxygen sensor replacement.',
            'Strange engine noises': 'Could be belt issues, low oil, or internal engine problems. Professional diagnosis recommended.'
        }
    },
    'hybrid': {
        'name': 'Hybrid Vehicles',
        'problems': {
            'Battery degradation': 'Regular battery health checks recommended. May require hybrid battery replacement after 100,000-150,000 miles.',
            'Regenerative braking issues': 'Check brake system and regenerative braking components. May need calibration or repair.',
            'Engine starting problems': 'Could be 12V battery issues or hybrid system faults. Diagnostic scan recommended.',
            'Reduced fuel efficiency': 'Check hybrid battery health, tire pressure, and driving habits. May need system recalibration.',
            'Warning light indicators': 'Perform diagnostic scan to identify hybrid system issues. Professional hybrid specialist recommended.'
        }
    },
    'ev': {
        'name': 'Electric Vehicles',
        'problems': {
            'Range anxiety': 'Check battery health, driving habits, and charging patterns. May need battery diagnostic.',
            'Charging issues': 'Verify charging equipment, connection quality. May require charging system inspection.',
            'Battery degradation': 'Regular battery health monitoring recommended. Consider battery replacement if significant capacity loss.',
            'Motor noise': 'Unusual noises may indicate motor bearing issues. Professional EV inspection recommended.',
            'Regenerative braking': 'System may need calibration or component inspection. Check brake system health.'
        }
    },
    'luxury': {
        'name': 'Luxury Vehicles',
        'problems': {
            'Electronic system failures': 'Diagnostic scan required. May need software updates or component replacement.',
            'Air suspension issues': 'Check for leaks, compressor function. May need air spring or compressor replacement.',
            'Complex warning lights': 'Professional diagnostic required. Could be sensor or system malfunctions.',
            'Infotainment problems': 'May need software update or system reset. Could require component replacement.',
            'Premium fuel requirements': 'Use recommended fuel grade to prevent engine knocking and performance issues.'
        }
    },
    'suv_truck': {
        'name': 'SUVs and Trucks',
        'problems': {
            'Suspension wear': 'Check shock absorbers, springs, and bushings. May need component replacement.',
            'Transmission strain': 'Regular transmission service recommended. Check towing habits and fluid condition.',
            'Alignment issues': 'Regular alignment checks recommended, especially after off-road use.',
            'Fuel efficiency': 'Check tire pressure, driving habits, and maintenance schedule. Consider aerodynamic improvements.',
            'Brake wear': 'Regular brake inspection recommended, especially if used for towing.'
        }
    },
    'vintage': {
        'name': 'Vintage/Classic Cars',
        'problems': {
            'Carburetor issues': 'Regular cleaning and adjustment needed. May require rebuild or replacement.',
            'Electrical problems': 'Check wiring condition, connections, and ground points. May need rewiring.',
            'Oil leaks': 'Identify leak sources, replace gaskets or seals as needed.',
            'Rust/corrosion': 'Regular inspection and prevention treatment recommended. May need professional restoration.',
            'Parts availability': 'Source reliable parts suppliers. Consider preventive maintenance to preserve original components.'
        }
    }
}

# Intent patterns and responses
intent_patterns = {
    'inappropriate_language': {
        'patterns': [
            'stupid', 'idiot', 'dumb', 'useless', 'garbage', 'trash',
            'fool', 'moron', 'incompetent', 'worthless', 'junk'
        ],
        'responses': [
            "I understand you might be frustrated, but let's maintain a respectful dialogue. How can I assist you with your car service needs?",
            "I'd be happy to help you, but we need to communicate respectfully. Could you please rephrase your request?",
            "Let's focus on solving your problem professionally. What specific assistance do you need with your vehicle?",
            "I'm here to help, but I can only do so in a respectful conversation. What car-related questions do you have?"
        ]
    },
    'welcome': {
        'patterns': ['welcome', 'start', 'begin', 'new'],
        'responses': [
            "Welcome to our Car Service App! 🚗\n\nI'm here to help you with:\n- Service Packages & Pricing\n- Vehicle Diagnostics\n- Maintenance Scheduling\n- Technical Support\n\nHow can I assist you today?",
            "Welcome to your automotive service assistant! 🔧\n\nI can help you with:\n- Service Bookings\n- Vehicle Problems\n- Maintenance Tips\n- Price Inquiries\n\nWhat would you like to know?",
            "Welcome aboard! I'm your car service expert. 🚘\n\nServices available:\n- Vehicle Checkups\n- Maintenance Packages\n- Problem Diagnosis\n- Appointment Scheduling\n\nHow may I help you?"
        ]
    },
    'greeting': {
        'patterns': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
        'responses': [
            "Hello! Welcome to our Auto Service Center! How may I assist you today?",
            "Hi there! Thank you for reaching out. What can I help you with?",
            "Welcome! How can I make your service experience better today?"
        ]
    },
    'service_inquiry': {
        'patterns': ['how much', 'cost', 'price', 'fee', 'charge'],
        'responses': {
            'oil_change': f"Our standard oil change starts at {service_pricing['oil_change']['price']} {service_pricing['oil_change']['currency']} and takes approximately {service_pricing['oil_change']['duration']} minutes.",
            'tire_rotation': f"Tire rotations cost {service_pricing['tire_rotation']['price']} {service_pricing['tire_rotation']['currency']} and can be completed in {service_pricing['tire_rotation']['duration']} minutes.",
            'brake_inspection': f"Our brake inspection costs {service_pricing['brake_inspection']['price']} {service_pricing['brake_inspection']['currency']} and takes about {service_pricing['brake_inspection']['duration']} minutes.",
            'general': "I can help you with pricing. Which service are you interested in? We offer:\n- Oil Change (ج.م. 600)\n- Tire Rotation (ج.م. 250)\n- Brake Inspection (ج.م. 400)"
        }
    },
    'technical_issue': {
        'patterns': ['noise', 'sound', 'problem', 'issue', 'light', 'warning', 'check'],
        'responses': {
            'noise': "I'm sorry to hear that. Could you describe the noise (e.g., grinding, squeaking) and when it occurs?",
            'brake': "This may indicate worn brake pads. Our inspection costs ج.م. 400 and takes 20 minutes. Would you like to schedule it?",
            'engine_light': "The check engine light can indicate various issues. We recommend a diagnostic scan. Would you like to schedule an inspection?",
            'general': "Could you provide more details about the issue? When did it start and under what conditions does it occur?"
        }
    },
    'appointment': {
        'patterns': ['book', 'schedule', 'appointment', 'reserve', 'set up'],
        'responses': {
            'confirm': "I can help you schedule an appointment. What day and time works best for you?",
            'success': "Great! Your appointment has been scheduled for [TIME]. We'll send a confirmation via SMS.",
            'followup': "Is there anything else you need to know about your upcoming service?"
        }
    },
    'human_request': {
        'patterns': ['human', 'person', 'agent', 'advisor', 'representative', 'speak', 'talk'],
        'responses': [
            "I'll connect you with our service advisor for further assistance. Please hold a moment.",
            "Let me transfer you to a specialist who can better assist you.",
            "I'm connecting you with our service team now."
        ]
    },
    'feedback': {
        'patterns': ['rate', 'review', 'feedback', 'experience'],
        'responses': [
            "How was your experience with us? Please rate us 1-5 stars.",
            "We value your feedback! How would you rate your recent service experience?",
            "Thank you for choosing us! Would you mind rating your experience from 1-5 stars?"
        ]
    },
    'service_packages': {
        'patterns': ['service package', 'maintenance package', 'service plan', 'available package', 'what package', 'show package', 'list package'],
        'responses': {
            'general': "Here are our service packages:\n\n1. Basic Service (ج.م. 2,999)\n- Every 5,000 km or 6 months\n- Basic maintenance and safety checks\n\n2. Standard Service (ج.م. 4,999)\n- Every 10,000 km or 12 months\n- Comprehensive maintenance\n\n3. Platinum Service (ج.م. 7,495)\n- Every 20,000 km or 18 months\n- Advanced diagnostics and service\n\n4. Comprehensive Service (ج.م. 9,495)\n- Every 40,000 km or 24 months\n- Complete vehicle overhaul\n\nWhich package would you like to know more about?",
            'basic': "Basic Service Package - ج.م. 2,999\nInterval: Every 5,000 km or 6 months\nIncludes:\n- Oil and filter change\n- Tire pressure check\n- Basic safety inspection\n- Fluid level check\n- Battery check",
            'standard': "Standard Service Package - ج.م. 4,999\nInterval: Every 10,000 km or 12 months\nIncludes:\n- All Basic Package services\n- Brake system inspection\n- Air filter replacement\n- Cabin filter check\n- Wheel alignment check\n- Belt and hose inspection",
            'platinum': "Platinum Service Package - ج.م. 7,495\nInterval: Every 20,000 km or 18 months\nIncludes:\n- All Standard Package services\n- Transmission fluid check\n- Spark plug replacement\n- Thorough brake service\n- AC system check\n- Advanced computer diagnostics",
            'comprehensive': "Comprehensive Service Package - ج.م. 9,495\nInterval: Every 40,000 km or 24 months\nIncludes:\n- All Platinum Package services\n- Major tune-up\n- Transmission service\n- Coolant system flush\n- Fuel system cleaning\n- Complete vehicle inspection"
        }
    },
}

# Preventive maintenance tips
maintenance_tips = {
    'general': [
        "Regular oil changes every 5,000-7,500 km",
        "Check tire pressure monthly",
        "Rotate tires every 10,000 km",
        "Replace air filter annually",
        "Check all fluids monthly"
    ],
    'seasonal': {
        'summer': [
            "Check AC system",
            "Monitor coolant levels",
            "Inspect battery condition",
            "Check brake fluid"
        ],
        'winter': [
            "Check heater and defroster",
            "Test battery strength",
            "Inspect wipers and washer fluid",
            "Check tire tread depth"
        ]
    },
    'mileage_based': {
        '5000km': ["Oil change", "Tire rotation", "Basic inspection"],
        '20000km': ["Brake service", "Transmission check", "Full inspection"],
        '40000km': ["Major service", "Timing belt check", "Comprehensive inspection"]
    }
}
