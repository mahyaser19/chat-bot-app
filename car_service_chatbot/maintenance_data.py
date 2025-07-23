"""
Extended vehicle maintenance data from MuneebAnsari's vehicle-maintenance-chatbot
"""

maintenance_procedures = {
    'oil_change': {
        'name': 'Oil Change Procedure',
        'steps': [
            'Park the car on level ground and engage parking brake',
            'Warm up the engine for 2-3 minutes',
            'Locate the oil drain plug under the car',
            'Place oil pan under drain plug',
            'Remove oil fill cap and drain plug',
            'Let old oil drain completely',
            'Replace drain plug with new washer',
            'Replace oil filter',
            'Add new oil through fill hole',
            'Check oil level with dipstick'
        ],
        'tools_needed': [
            'Oil pan',
            'Socket wrench set',
            'Oil filter wrench',
            'Funnel',
            'New oil filter',
            'New oil (check manual for type/quantity)',
            'New drain plug washer'
        ],
        'safety_notes': [
            'Never work under a car supported only by a jack',
            'Use jack stands for safety',
            'Wear safety glasses and gloves',
            'Be careful of hot oil if engine was recently running'
        ]
    },
    'brake_service': {
        'name': 'Brake Pad Replacement',
        'steps': [
            'Loosen wheel lug nuts while car is on ground',
            'Jack up car and secure with jack stands',
            'Remove wheels',
            'Remove brake caliper bolts',
            'Suspend caliper with wire hook',
            'Remove old brake pads',
            'Clean caliper and rotor',
            'Install new brake pads',
            'Reinstall caliper',
            'Reinstall wheels and lower car'
        ],
        'tools_needed': [
            'Jack and jack stands',
            'Lug wrench',
            'Socket set',
            'Wire hook',
            'Brake cleaner',
            'New brake pads',
            'Anti-squeal brake paste',
            'C-clamp for caliper piston'
        ],
        'safety_notes': [
            'Always use jack stands',
            'Wear safety glasses',
            'Test brakes before driving',
            'Break in new pads properly'
        ]
    },
    'tire_rotation': {
        'name': 'Tire Rotation',
        'steps': [
            'Park on level ground, engage parking brake',
            'Loosen all wheel lug nuts while car is down',
            'Jack up car and place on jack stands',
            'Remove all wheels',
            'Check tire condition and pressure',
            'Rotate tires according to pattern',
            'Reinstall wheels with proper torque',
            'Lower car and final torque check'
        ],
        'tools_needed': [
            'Jack and jack stands',
            'Lug wrench',
            'Torque wrench',
            'Tire pressure gauge'
        ],
        'safety_notes': [
            'Use proper jack points',
            'Always use jack stands',
            'Torque lug nuts in star pattern',
            'Check tire pressures when cold'
        ]
    },
    'air_filter': {
        'name': 'Air Filter Replacement',
        'steps': [
            'Locate air filter housing',
            'Open air filter housing',
            'Note orientation of old filter',
            'Remove old air filter',
            'Clean housing of debris',
            'Install new filter in correct orientation',
            'Close and secure housing'
        ],
        'tools_needed': [
            'Screwdriver or socket set (varies by vehicle)',
            'New air filter',
            'Cleaning cloth'
        ],
        'safety_notes': [
            'Ensure engine is off and cool',
            'Don\'t drop debris into intake',
            'Verify filter orientation'
        ]
    }
}

# Arabic translations of maintenance procedures
maintenance_procedures_ar = {
    'oil_change': {
        'name': 'إجراءات تغيير الزيت',
        'steps': [
            'اركن السيارة على أرض مستوية وشغل فرامل اليد',
            'قم بتسخين المحرك لمدة 2-3 دقائق',
            'حدد موقع سدادة تصريف الزيت تحت السيارة',
            'ضع وعاء الزيت تحت سدادة التصريف',
            'قم بإزالة غطاء تعبئة الزيت وسدادة التصريف',
            'دع الزيت القديم يتصرف بالكامل',
            'استبدل سدادة التصريف بحلقة جديدة',
            'استبدل فلتر الزيت',
            'أضف الزيت الجديد من خلال فتحة التعبئة',
            'تحقق من مستوى الزيت باستخدام عصا القياس'
        ],
        'tools_needed': [
            'وعاء زيت',
            'طقم مفاتيح شد',
            'مفتاح فلتر الزيت',
            'قمع',
            'فلتر زيت جديد',
            'زيت جديد (راجع الدليل لمعرفة النوع/الكمية)',
            'حلقة سدادة تصريف جديدة'
        ],
        'safety_notes': [
            'لا تعمل أبداً تحت سيارة مدعومة فقط برافعة',
            'استخدم حوامل الرافعة للسلامة',
            'ارتدِ نظارات وقفازات السلامة',
            'احذر من الزيت الساخن إذا كان المحرك يعمل مؤخراً'
        ]
    },
    'brake_service': {
        'name': 'استبدال بطانات الفرامل',
        'steps': [
            'فك صواميل العجلات والسيارة على الأرض',
            'ارفع السيارة وثبتها بحوامل الرافعة',
            'فك العجلات',
            'فك مسامير الفرامل',
            'علق المكبح بخطاف سلكي',
            'أزل بطانات الفرامل القديمة',
            'نظف المكبح والقرص',
            'ركب بطانات فرامل جديدة',
            'أعد تركيب المكبح',
            'أعد تركيب العجلات وأنزل السيارة'
        ],
        'tools_needed': [
            'رافعة وحوامل رافعة',
            'مفتاح عجل',
            'طقم مفاتيح شد',
            'خطاف سلكي',
            'منظف فرامل',
            'بطانات فرامل جديدة',
            'معجون منع صرير الفرامل',
            'مشبك C لمكبس المكبح'
        ],
        'safety_notes': [
            'استخدم دائماً حوامل الرافعة',
            'ارتدِ نظارات السلامة',
            'اختبر الفرامل قبل القيادة',
            'قم بتليين البطانات الجديدة بشكل صحيح'
        ]
    }
}

diagnostic_procedures = {
    'engine_noise': {
        'symptoms': [
            'Knocking sound',
            'Ticking noise',
            'Squealing',
            'Rumbling'
        ],
        'possible_causes': [
            'Low oil level',
            'Worn bearings',
            'Loose belt',
            'Exhaust leak'
        ],
        'diagnostic_steps': [
            'Check oil level and condition',
            'Listen for noise location',
            'Check belt tension',
            'Inspect exhaust system'
        ]
    },
    'brake_problems': {
        'symptoms': [
            'Squeaking',
            'Grinding',
            'Vibration',
            'Soft pedal'
        ],
        'possible_causes': [
            'Worn brake pads',
            'Warped rotors',
            'Air in brake lines',
            'Caliper issues'
        ],
        'diagnostic_steps': [
            'Visual inspection of pads',
            'Check rotor condition',
            'Test brake pedal feel',
            'Inspect brake fluid'
        ]
    }
}

# Arabic translations of diagnostic procedures
diagnostic_procedures_ar = {
    'engine_noise': {
        'symptoms': [
            'صوت طرق',
            'صوت تكتكة',
            'صوت صرير',
            'صوت هدير'
        ],
        'possible_causes': [
            'مستوى زيت منخفض',
            'تآكل المحامل',
            'حزام مرتخي',
            'تسرب في العادم'
        ],
        'diagnostic_steps': [
            'فحص مستوى وحالة الزيت',
            'تحديد موقع الصوت',
            'فحص شد الحزام',
            'فحص نظام العادم'
        ]
    },
    'brake_problems': {
        'symptoms': [
            'صرير',
            'صوت طحن',
            'اهتزاز',
            'دواسة لينة'
        ],
        'possible_causes': [
            'تآكل بطانات الفرامل',
            'تشوه الأقراص',
            'هواء في خطوط الفرامل',
            'مشاكل في المكابح'
        ],
        'diagnostic_steps': [
            'فحص بصري للبطانات',
            'فحص حالة القرص',
            'اختبار إحساس دواسة الفرامل',
            'فحص سائل الفرامل'
        ]
    }
}
