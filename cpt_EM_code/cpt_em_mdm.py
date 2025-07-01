from openaiWrapper import gpt_mdm_problem, gpt_mdm_data, gpt_mdm_morbidity, gpt_make_reasoning_concise
import json
from cpt_EM_code.json_schema import RISK_SCHEMA, PROBLEM_SCHEMA, DATA_SCHEMA, REASON_SCHEMA


def cpt_mdm_problem(transcription = "", summary = ""):
    json_data_str = gpt_mdm_problem(transcription, summary, PROBLEM_SCHEMA)
    json_data = json.loads(json_data_str)
    print("problem output : ", json_data_str)
    intensity, reason = mdm_problem_rule_engine(json_data)
    return intensity, reason

def mdm_problem_rule_engine(data):
    # print(data)
    if "questions" not in data:
        return False, ""
    questions = data["questions"]
    reasoning = ""
    # high
    if '12' in questions or '11' in questions:
        if int(questions['12']['answer'])>=1 or int(questions['11']['answer'])>=1:
            reasoning += questions['12']['explanation'] +". "
            reasoning += questions['11']['explanation'] +". "
            # its high
            return 4, reasoning
    # moderate
    if '7' in questions or '3'in questions or '8'in questions or '9'in questions or '10'in questions:
        if int(questions['7']['answer'])>=1 or int(questions['3']['answer'])>=2 or int(questions['8']['answer'])>=1 or int(questions['9']['answer'])>=1 or int(questions['10']['answer'])>=1:
            reasoning += questions['7']['explanation'] +". "
            reasoning += questions['3']['explanation'] +". "
            reasoning += questions['8']['explanation'] +". "
            reasoning += questions['9']['explanation'] +". "
            reasoning += questions['10']['explanation'] +". Makes this moderate problem."
            # its moderate
            return 3, reasoning
    # low
    if '2' in questions or '3' in questions or '4' in questions or '5' in questions or '6' in questions:
        if int(questions['2']['answer'])>=2 or int(questions['3']['answer'])>=2 or int(questions['4']['answer'])>=1 or int(questions['5']['answer'])>=1 or int(questions['6']['answer'])>=1:
            reasoning += questions['2']['explanation'] +". "
            reasoning += questions['3']['explanation'] +". "
            reasoning += questions['4']['explanation'] +". "
            reasoning += questions['5']['explanation'] +". "
            reasoning += questions['6']['explanation'] +". Makes this low problem."
            # its low
            return 2, reasoning
        
    # minimal
    if '2' in questions :
        if int(questions['2']['answer'])>=1 :
            # its miniamal
            print("problem : ", "minimal")
            reasoning += questions['2']['explanation'] +". Makes this minimal problem."
            return 1, reasoning

    return 1, "no any problems. Hence minimal problem"

def cpt_mdm_data(transcription, summary):
    json_data_str = gpt_mdm_data(transcription, summary, DATA_SCHEMA)
    json_data = json.loads(json_data_str)
    intensity, reason = mdm_data_rule_engine(json_data)
    return intensity, reason

def mdm_data_rule_engine(data):
    if "questions" not in data:
        return False
    questions = data["questions"]
    #category 1_a:
    cat_1a_count = 0
    reasoning = ""
    if questions["1"]["answer"] =='yes':
        reasoning += questions["1"]["explanation"] + ". "
        cat_1a_count+=1
    if questions["2"]["answer"] =='yes':
        reasoning += questions["2"]["explanation"] + ". "
        cat_1a_count+=1
    if questions["3"]["answer"] =='yes':
        reasoning += questions["3"]["explanation"] + ". "
        cat_1a_count+=1

    cat_1b_count = cat_1a_count
    if questions["4"]["answer"] =='yes':
        reasoning += questions["4"]["explanation"] + ". "
        cat_1b_count+=1

    cat_2_count = 0
    if questions["5"]["answer"] =='yes':
        reasoning += questions["5"]["explanation"] + ". "
        cat_2_count+=1
    
    cat_3_count = 0
    if questions["6"]["answer"] =='yes':
        reasoning += questions["6"]["explanation"] + ". "
        cat_3_count+=1
    
    if cat_1a_count >= 3:
        cat_1a_count = 1

    if cat_1b_count >= 2:
        cat_1b_count = 1
    
    #high
    high_count = cat_1b_count + cat_2_count + cat_3_count
    low_count = cat_1a_count + cat_2_count
    if high_count >= 2:
        reasoning += "Which puts it in high data analyzed."
        return 4, reasoning

    if high_count >= 1:
        reasoning += "Which puts it in moderate data analyzed."
        return 3, reasoning

    if low_count >= 1:
        reasoning += "Which puts it in low data analyzed."
        return 2, reasoning

    reasoning += " minimal data analyzed."
    return 1, reasoning

def cpt_mdm_morbidity(transcription, summary):
    json_data_str = gpt_mdm_morbidity(transcription, summary, RISK_SCHEMA)
    json_data = json.loads(json_data_str)
    intensity, reason = mdm_morbidity_rule_engine(json_data)
    return intensity, reason

def mdm_morbidity_rule_engine(data):
    # print(data)
    if "questions" not in data:
        return False
    questions = data["questions"]
    if questions["4"]["answer"] =='yes':
        reasoning = questions["4"]["explanation"] + ". Makes this High risk."
        return 4, reasoning
    if questions["3"]["answer"] =='yes':
        reasoning = questions["3"]["explanation"] + ". Makes this Moderate risk."
        return 3, reasoning
    if questions["2"]["answer"] =='yes':
        reasoning = questions["2"]["explanation"] + ". Makes this Low risk."
        return 2, reasoning
    if questions["1"]["answer"] =='yes':
        reasoning = questions["1"]["explanation"] + ". Makes this minimal risk."
        return 1, reasoning
    return 1, "no major risk involved"

def get_cpt_mdm_code(final_score, data):
    mdm_table = {
        "1":"",
        "2":"",
        "3":"",
        "4":"",
    }
    if "service_setting" not in data:
        return False
    if data["service_setting"] in ["office", "other opd", "opd"] and "patient_type" in data:
        if data["patient_type"] == "new":
            mdm_table = {
                "1":"99202",
                "2":"99203",
                "3":"99204",
                "4":"99205"
            }
        elif  data["patient_type"] == "established":
            mdm_table = {
                "1":"99212",
                "2":"99213",
                "3":"99214",
                "4":"99215"
            }
    if data["service_setting"] in ["ipd", "observation care"]:
        if "service_number" in data:
            if data["service_number"] == "initial":
                mdm_table = {
                    "1":"99221",
                    "2":"99221",
                    "3":"99222",
                    "4":"99223"
                }
            else:
                mdm_table = {
                    "1":"99231",
                    "2":"99231",
                    "3":"99232",
                    "4":"99233"
                }
    if data["service_setting"] in ["ipd admission and discharge"]:
        mdm_table = {
            "1":"99234",
            "2":"99234",
            "3":"99235",
            "4":"99236"
        } 
    if data["service_setting"] in ["ipd consultation", "observation consultation"]:
        mdm_table = {
            "1":"99252",
            "2":"99253",
            "3":"99254",
            "4":"99255"
        } 
    if data["service_setting"] in ["emergency"]:
        mdm_table = {
            "1":"99282",
            "2":"99283",
            "3":"99284",
            "4":"99285"
        }
    if data["service_setting"] in ["nursing"]:
        if "service_number" in data:
            if data["service_number"] == "initial":
                mdm_table = {
                    "1":"99304",
                    "2":"99304",
                    "3":"99305",
                    "4":"99306"
                }
            else:
                mdm_table = {
                    "1":"99307",
                    "2":"99308",
                    "3":"99309",
                    "4":"99310"
                }
                
    if data["service_setting"] in ["residence"]:
        if data["patient_type"] == "new":
            mdm_table = {
                "1":"99341",
                "2":"99342",
                "3":"99344",
                "4":"99345"
            }
        elif  data["patient_type"] == "established":
            mdm_table = {
                "1":"99347",
                "2":"99348",
                "3":"99349",
                "4":"99350"
            }
        
    return mdm_table[str(final_score)]

def make_reasoning_concise(reasoning):
    json_data_str = gpt_make_reasoning_concise(reasoning, REASON_SCHEMA)
    json_data = json.loads(json_data_str)
    if "reasoning" in json_data:
        return json_data["reasoning"]
    return ""
     

def cpt_mdm_driver(data):
    transcription = ""
    summary = ""
    if "transcription"  in data:
        transcription = data["transcription"]
    if "summary" in data:
        summary = data["summary"]
    print("problem_started")
    intensity_1, reasoning_1 = cpt_mdm_problem(transcription, summary)
    print("data_started")
    intensity_2, reasoning_2 = cpt_mdm_data(transcription, summary)
    print("morbidity_started")
    intensity_3, reasoning_3 = cpt_mdm_morbidity(transcription, summary)
    # intensity_1, intensity_2, intensity_3 = 4,4,4
    print("score1,2,3:", intensity_1,":", intensity_2,":", intensity_3)
    print("resoning_1 : ",  reasoning_1)
    print("resoning_1 : ",  reasoning_2)
    print("resoning_1 : ",  reasoning_3)
    raw_reason = "From the visit details we can conclude the follwoing informations. " + reasoning_1+reasoning_2+reasoning_3
    reason = make_reasoning_concise(raw_reason)
    print("reasoning : ",  reason)

    total_sum_score = intensity_1 + intensity_2 + intensity_3
    min_score = min(intensity_1 , intensity_2 , intensity_3)
    max_score = max(intensity_1 , intensity_2 , intensity_3)
    total_sum_score = total_sum_score - min_score
    final_score = total_sum_score - max_score
    print("final_score : ", final_score)
    cpt_code = get_cpt_mdm_code(final_score, data)
    return cpt_code, reason


# transcription_20 = """Physician (Dr. Patel):
# Good afternoon, Ms. Carter. I see you're here for your annual preventive visit and to discuss the hepatitis B vaccine for your new job. How have you been feeling overall?

# Patient (Ms. Carter):
# Hi, Dr. Patel. I've been doing okay. I'm here for the vaccine since my job said it was recommended, but I'm also dealing with some lower abdominal pain.

# Dr. Patel:
# Got it. We'll make sure to address both. First, let's go over your preventive health. This visit is a good time to review everything, including any lab work or screenings you might need based on your age and medical history. You're diabetic, but your recent tests show that your blood sugar levels are stable, which is great. How's your diabetes management going?

# Ms. Carter:
# It's been fine. I'm sticking to my medications and watching my diet, though it's hard sometimes.

# Dr. Patel:
# You're doing well. Keep up the good work with your diet and medications. I'll provide some additional resources if you need them, but overall, your diabetes seems to be under good control. Now, about the hepatitis B vaccine—since your lab results showed low immunity, it's a good idea to get vaccinated to protect yourself, especially in your new job. It's a safe and effective vaccine.

# Ms. Carter:
# I was all set to get it, but when I reviewed my employee health form again, I saw that it's optional. Do I really need it?

# Dr. Patel:
# While it might be optional for your job, hepatitis B is a serious infection that can cause long-term liver damage. The vaccine is recommended, especially if your immunity is low. It's a personal choice, but getting vaccinated would provide extra protection, particularly in environments where you may come into contact with blood or bodily fluids.

# Ms. Carter:
# I'm not sure anymore. Since it's optional, I think I'll skip it for now.

# Dr. Patel:
# That's okay. If you change your mind later, we can easily schedule it. I just want to make sure you're fully informed of the benefits. Now, let's shift to your abdominal pain. Can you describe it a bit more?

# Ms. Carter:
# It's been this dull ache in my lower abdomen for a few days. It's not sharp, but it's uncomfortable, especially when I move around a lot.

# Dr. Patel:
# I see. I'll conduct a physical exam to get a better understanding of what might be causing it. Based on your description, we'll want to check for any signs of infection or other underlying issues.

# (Dr. Patel performs a physical examination.)

# Dr. Patel:
# From the exam, it looks like you might have a mild case of pelvic inflammatory disease (PID), which could be causing the discomfort. I'm going to prescribe you some antibiotics to treat the infection. It's important to take the full course of medication, even if you start feeling better before you finish it.

# Ms. Carter:
# Okay. Is there anything I need to watch out for?

# Dr. Patel:
# Yes, I'll go over the risks and benefits of the medication with you. The antibiotics are generally well-tolerated, but you might experience mild side effects like nausea or stomach upset. If you have any severe reactions, such as a rash or difficulty breathing, stop taking the medication and contact me immediately. It's also important to avoid missing doses to make sure the infection clears up completely.

# Ms. Carter:
# Got it. I'll be careful with that.

# Dr. Patel:
# Great. I'll send your prescription to the pharmacy, and we'll follow up if necessary. Now that we've covered everything, I'll go ahead and update your records. If you have any other concerns, don't hesitate to reach out.

# Ms. Carter:
# Thanks, Dr. Patel. I appreciate your help today.

# Dr. Patel:
# You're welcome. Take care, and I'll see you for your next follow-up.

# """
# transcription_21 = """Setting: Mr. Johnson's living room, where Dr. Smith is visiting for a home evaluation.

# Dr. Smith: Good morning, Mr. Johnson. How are you feeling today?

# Mr. Johnson: Good morning, Doctor. I'm managing, but I've been having more trouble getting around lately.

# Dr. Smith: I'm sorry to hear that. Mobility issues can really affect your quality of life. Can you tell me more about the difficulties you're experiencing?

# Mr. Johnson: Well, my legs feel weak, and I sometimes lose my balance. It's making it hard to get to the bathroom or even just move around the house.

# Dr. Smith: I understand. Let's take a look at your overall health and see how we can help with that. First, I'd like to check your blood sugar levels since you have diabetes. Have you been monitoring it regularly?

# Mr. Johnson: Yes, I check it daily, but it seems to fluctuate a lot. Sometimes it's high, and other times it's too low.

# Dr. Smith: Fluctuations can be tricky. I'll review your medications and diet to see if we can stabilize your blood sugar. Now, let's also discuss your COPD. Have you noticed any changes in your breathing?

# Mr. Johnson: Yes, I get short of breath more easily, especially when I'm moving around or doing small tasks.

# Dr. Smith: That's important to note. We'll assess your lung function today. It might also help to adjust your medications if you're experiencing more symptoms. Now, regarding your chronic pain, where do you feel it most?

# Mr. Johnson: It's mostly in my back and knees. Sometimes it gets really bad and makes it hard to walk.

# Dr. Smith: I see. Pain management is crucial for your mobility. I'll examine those areas and see if we can adjust your pain management plan. Let's start with a comprehensive examination.

# (Dr. Smith conducts the physical exam, assessing Mr. Johnson's mobility, checking his blood pressure, listening to his lungs, and examining his back and knees.)

# Dr. Smith: Everything looks a bit concerning. Your blood pressure is a bit high, and your lung sounds indicate some wheezing. We may need to adjust your COPD medications.

# Mr. Johnson: That makes sense. I've been feeling more fatigued too.

# Dr. Smith: Fatigue can be linked to both your diabetes management and your COPD. We need to ensure that all your medications are balanced. Let's go over your medication list.

# (Dr. Smith reviews Mr. Johnson's medications.)

# Dr. Smith: I see you're taking Metformin for your diabetes, but we might consider adding another medication to help stabilize your blood sugar. For your COPD, we can increase your bronchodilator dosage. I'll also prescribe something for your pain management that's less likely to affect your mobility.

# Mr. Johnson: I appreciate that. I just want to feel better and be able to move around without fear of falling.

# Dr. Smith: Absolutely, Mr. Johnson. It's all about improving your quality of life. I'll write up new prescriptions and also refer you to a physical therapist who can work with you on strength and balance exercises.

# Mr. Johnson: That sounds like a great plan. Thank you for taking the time to come here and help me out.

# Dr. Smith: My pleasure. I'll also provide you with educational materials about managing your diabetes and COPD at home. Remember, it's important to follow up regularly, so let's schedule our next visit in about a month.

# Mr. Johnson: Thank you, Doctor. I feel better just talking about it and having a plan in place.

# """
# summary_1 = """Office visit for an established adolescent
# patient with a history of bipolar disorder
# treated with lithium; seen on an urgent
# basis at family's request because of severe
# depressive symptoms."""
# summary_8 ="""
# A 14-year-old female patient with a history of cystic acne arrives to her dermatology oncology initial visit for treatment. She was referred by her general dermatologist who belongs to the same practice. The provider carried out a comprehensive history and exam and reviewed the patient's chart which contained a comprehensive metabolic, renal, and thyroid panels with a skin biopsy.
# Final diagnostic statement: Chronic cystic acne
# Total time: Total time of the encounter 60 minutes"""
# data = {
#     # "transcription":transcription_14,
#     "summary" : summary_8,
#     "patient_type" :  "new",
#     "service_setting": "opd",
#     "service_number" : "initial"
# }
# print(cpt_mdm_driver(data))
