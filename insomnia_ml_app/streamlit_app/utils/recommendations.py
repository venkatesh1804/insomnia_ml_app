def get_recommendations(severity):
    """Get personalized recommendations based on severity with actionable, evidence-based advice"""
    
    recommendations = {
        'No Insomnia': {
            'title': '✅ Excellent Sleep Health Detected!',
            'message': 'Your sleep patterns are healthy and normal. Keep up the great work! Continue these habits to maintain optimal sleep quality and prevent future issues.',
            'tips': [
                '🌙 Maintain a consistent sleep schedule - Go to bed and wake up at the same time every day, even on weekends (±30 min max)',
                '🛏️ Optimize your sleep environment - Keep bedroom temperature between 60-67°F (15-19°C), use blackout curtains, and minimize noise',
                '📱 Digital sunset routine - Stop all screens (phone, TV, computer) 60-90 minutes before bedtime to avoid blue light disruption',
                '☕ Smart caffeine management - Avoid caffeine after 2 PM; switch to herbal tea or water in the afternoon',
                '🏃 Regular physical activity - Exercise 20-30 minutes daily, preferably in the morning or early afternoon (not within 3 hours of bedtime)',
                '🧘 Wind-down ritual - Develop a relaxing 30-minute bedtime routine: reading, gentle stretching, meditation, or warm bath',
                '🍽️ Evening eating habits - Finish dinner 2-3 hours before bed; if hungry, opt for light snacks like banana, almonds, or warm milk',
                '☀️ Morning sunlight exposure - Get 10-30 minutes of natural light within 2 hours of waking to regulate your circadian rhythm'
            ],
            'duration': 'Maintain these habits daily for long-term sleep health'
        },
        'Mild': {
            'title': '⚠️ Mild Insomnia - Early Intervention Works!',
            'message': 'You are experiencing mild sleep difficulties. The good news: small, consistent changes can restore healthy sleep patterns within a few weeks. Start with sleep hygiene improvements and behavioral techniques.',
            'tips': [
                '⏰ Strict sleep schedule - Wake up at the same time every day (even weekends) and only go to bed when genuinely sleepy (not just tired)',
                '🛌 The 15-minute rule - If you cannot fall asleep within 15-20 minutes, get up and do a calm activity (reading, light stretching) in dim light until sleepy',
                '🧠 Cognitive techniques - When worrying in bed, mentally postpone concerns to "tomorrow\'s worry time" and practice 4-7-8 breathing (inhale 4 sec, hold 7 sec, exhale 8 sec)',
                '📓 Keep a sleep diary - Track sleep/wake times, naps, caffeine, exercise, and stress levels for 2 weeks to identify patterns',
                '☕ Zero caffeine after 12 PM - Caffeine has a 5-6 hour half-life; even afternoon coffee can disrupt sleep',
                '🌅 Morning light therapy - Get bright light exposure (outdoors or light therapy lamp) for 20-30 minutes within 1 hour of waking',
                '🚫 Limit daytime naps - If you must nap, keep it under 20 minutes and before 2 PM',
                '🍷 Avoid alcohol as sleep aid - While it may help you fall asleep, alcohol disrupts REM sleep and causes middle-of-night awakenings',
                '💪 Daily exercise - Aim for 30 minutes of moderate aerobic exercise, but complete it at least 4-6 hours before bedtime',
                '📱 Create a phone charging station - Keep your phone out of the bedroom entirely to reduce sleep disruptions and blue light exposure'
            ],
            'duration': '2-4 weeks for noticeable improvement with consistent application'
        },
        'Moderate': {
            'title': '🏥 Moderate Insomnia - Professional Support Recommended',
            'message': 'You have moderate insomnia that is likely impacting your daily functioning. Professional guidance is strongly recommended. Cognitive Behavioral Therapy for Insomnia (CBT-I) is the gold-standard first-line treatment with long-term effectiveness.',
            'tips': [
                '👨‍⚕️ Schedule sleep specialist appointment - Consult a sleep medicine physician or psychologist trained in CBT-I within the next 1-2 weeks',
                '🧠 Start CBT-I therapy - This 4-8 week structured program has 70-80% success rate and provides lasting results without medication',
                '⏱️ Sleep restriction therapy - Paradoxically limit time in bed to match actual sleep time, then gradually increase as sleep efficiency improves (do this under professional guidance)',
                '🛏️ Strict stimulus control - Only use your bed for sleep and intimacy; no reading, TV, phone, or worrying in bed. Leave bedroom if awake for 20+ minutes',
                '📊 Comprehensive sleep diary - Track detailed sleep metrics: bedtime, sleep latency, night awakenings, wake time, total sleep time, daytime functioning',
                '🧘 Progressive Muscle Relaxation (PMR) - Practice tensing and relaxing muscle groups from toes to head for 15-20 minutes before bed',
                '💭 Cognitive restructuring - Challenge catastrophic thoughts about sleep ("I\'ll never sleep again") and replace with realistic ones ("I\'ve had bad nights before and managed fine")',
                '🚫 Eliminate sleep saboteurs - Remove all caffeine, avoid alcohol within 4 hours of bed, no nicotine within 2 hours of sleep',
                '🏃 Structured exercise program - 30-45 minutes of moderate-to-vigorous aerobic exercise 4-6 days per week, preferably in morning or early afternoon',
                '🌡️ Optimize bedroom conditions - Use white noise machine for noise masking, keep temperature at 65-68°F, ensure mattress and pillows are comfortable',
                '📱 Blue light blocking - Use blue light blocking glasses 2-3 hours before bed if screen use is unavoidable',
                '⚕️ Medical evaluation - Rule out underlying conditions: sleep apnea, restless leg syndrome, thyroid issues, chronic pain, depression, anxiety'
            ],
            'duration': '4-8 weeks of CBT-I for significant improvement; ongoing practice for maintenance'
        },
        'Severe': {
            'title': '🚨 Severe Insomnia - Immediate Medical Intervention Required',
            'message': 'You have severe chronic insomnia that requires urgent professional medical attention. This level of sleep disruption significantly impacts health, safety, and quality of life. Do not delay seeking help - effective treatments are available.',
            'tips': [
                '🏥 URGENT: Book sleep specialist - Schedule appointment with board-certified sleep medicine physician or psychiatrist within 1 week; request urgent/priority appointment',
                '🛌 Request sleep study (polysomnography) - Comprehensive overnight testing can identify sleep disorders like sleep apnea, periodic limb movement disorder, or other conditions requiring specific treatment',
                '💊 Medical intervention discussion - Discuss short-term prescription sleep medications (e.g., cognitive-behavioral therapy + medication combo) with your doctor as a bridge to long-term solutions',
                '🧠 Intensive CBT-I program - Enroll in intensive 6-8 week CBT-I program, possibly including group therapy sessions (highly effective even for severe insomnia)',
                '🏥 Consider sleep rehabilitation center - For severe cases, inpatient or intensive outpatient sleep disorder programs provide comprehensive multidisciplinary care',
                '🩺 Comprehensive medical workup - Full evaluation for contributing conditions: depression, anxiety disorders, PTSD, chronic pain, medications side effects, hormonal imbalances',
                '⏰ Sleep restriction protocol - Under professional supervision, restrict time in bed to actual sleep time (may start with just 5-6 hours) to rebuild sleep drive',
                '📊 Digital sleep monitoring - Use sleep tracking devices or apps to provide objective data to your healthcare provider (Fitbit, Oura Ring, Apple Watch)',
                '🧘 Mindfulness-Based Therapy - Combine CBT-I with Mindfulness-Based Stress Reduction (MBSR) or Acceptance and Commitment Therapy (ACT) for anxiety about sleep',
                '💪 Supervised exercise program - Work with physical therapist or trainer to establish safe, regular exercise routine that supports sleep',
                '🍽️ Nutritional support - Consult nutritionist about foods that support sleep: magnesium-rich foods (almonds, spinach), tryptophan sources (turkey, eggs, cheese)',
                '🧑‍⚕️ Medication management - If taking sleep medications, work closely with doctor on proper dosing, timing, tapering strategies, and avoiding dependency',
                '👥 Support system - Join insomnia support group (online or in-person) and educate family/friends about your condition for emotional support',
                '📱 Safety precautions - Avoid driving when severely sleep-deprived; discuss work accommodations or medical leave if needed for treatment'
            ],
            'duration': '3-6 months of intensive treatment with ongoing monitoring; expect gradual improvement with professional guidance'
        }
    }
    
    return recommendations.get(severity, recommendations['Severe'])