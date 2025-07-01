from datetime import timedelta
# from cpt_sections.section_wise_cpt import critical_care_time_based, psychotherapy_time_based
transcript = {
    "I have been having severe chest pain for the last few hours.": {
      "start_time": 0,
      "end_time": 4
    },
    "Its not moving a bit and its really scary pain.": {
      "start_time": 4,
      "end_time": 7
    },
    "I understand Robin. Lets take it step by step.": {
      "start_time": 7,
      "end_time": 10
    },
    "Can you describe the pain in more detail? Is it constant or does it come and go?": {
      "start_time": 10,
      "end_time": 13
    },
    "Its been constant and it feels like a heavy pressure.": {
      "start_time": 13,
      "end_time": 16
    },
    "It started a few hours ago and it hasnt let up since.": {
      "start_time": 16,
      "end_time": 20
    },
    "Its hard to catch my breath sometimes.": {
      "start_time": 20,
      "end_time": 22
    },
    "Alright. Any pain when I press on your chest or any sharp pain when you breathe in deeply?": {
      "start_time": 22,
      "end_time": 27
    },
    "No, not really. The pressure is inside, not on the surface.": {
      "start_time": 27,
      "end_time": 31
    },
    "Im not hearing any murmurs in your heart and your lungs sound clear which is a good sign.": {
      "start_time": 31,
      "end_time": 35
    },
    "But chest pain like this, especially with your history of hypertension needs to be taken very seriously.": {
      "start_time": 35,
      "end_time": 40
    },
    "We need to rule out any heart related causes or the serious conditions. Doctor, her blood pressure is 160 over 100, heart rate is 110 and oxygen saturation is 94%.": {
      "start_time": 40,
      "end_time": 50.18
    },
    "Heres the ECG report we just ran.": {
      "start_time": 50.18,
      "end_time": 52.06
    },
    "We also set up the IV.": {
      "start_time": 52.3,
      "end_time": 53.4
    },
    "No past history of heart issues but shes on amlodipine for hypertension and she just started trulicity for her diabetes.": {
      "start_time": 54.04,
      "end_time": 58.92
    },
    "Thanks.": {
      "start_time": 59.9,
      "end_time": 60.3
    },
    "Hmm, Robin, it looks like theres something showing up here.": {
      "start_time": 60.94,
      "end_time": 63.28
    },
    "You see this part of the ECG, the ST segment?": {
      "start_time": 63.5,
      "end_time": 65.4
    },
    "Its slightly depressed, which can sometimes indicate reduced blood flow to the heart.": {
      "start_time": 65.78,
      "end_time": 68.92
    },
    "This pattern is typical in angina, where the heart isnt receiving enough blood supply,": {
      "start_time": 69.32,
      "end_time": 73.44
    },
    "especially during times of stress.": {
      "start_time": 73.84,
      "end_time": 75.3
    },
    "Angina? So its not a heart attack?": {
      "start_time": 76.06,
      "end_time": 78.64
    },
    "Right now, it looks more like angina than a full-blown heart attack, which is a good thing.": {
      "start_time": 79.14,
      "end_time": 82.96
    },
    "Angina means that your heart isnt getting enough blood flow but its not causing permanent damage": {
      "start_time": 83.52,
      "end_time": 87.2
    },
    "like a heart attack would. Still, we need to act quickly to prevent anything from escalating.": {
      "start_time": 87.2,
      "end_time": 92.2
    },
    "So what happens next? First, Im ordering cardiac enzyme tests through": {
      "start_time": 92.2,
      "end_time": 96.12
    },
    "blood work. This will help us confirm that theres no ongoing damage to your heart. Well": {
      "start_time": 96.12,
      "end_time": 100.5
    },
    "also do a chest x-ray to rule out any lung issues that could be contributing to the pain.": {
      "start_time": 100.5,
      "end_time": 104.6
    },
    "Im continuing your current medication but Im going to give you oral nitroglycerin immediately.": {
      "start_time": 104.6,
      "end_time": 108.68
    },
    "It will help relieve the chest pain by dilating your blood vessels and allowing more blood to flow to your heart.": {
      "start_time": 108.68,
      "end_time": 113.68
    },
    "Ill administer the nitroglycerin now, doctor.": {
      "start_time": 113.68,
      "end_time": 116.32
    },
    "Am I going to be okay, doctor?": {
      "start_time": 116.32,
      "end_time": 119.08
    },
    "Robin, were taking all the necessary steps to make sure youre stable.": {
      "start_time": 119.08,
      "end_time": 122.48
    },
    "Angina is manageable but its important to keep you monitored here for the next few days. Well run the": {
      "start_time": 122.48,
      "end_time": 127.6
    },
    "tests, get the results and adjust your treatments as needed. The good news is": {
      "start_time": 127.6,
      "end_time": 131.64
    },
    "that weve got this early so we can take action before it becomes more serious.": {
      "start_time": 131.64,
      "end_time": 134.94
    },
    "Thats reassuring. I just want this pain to go away. I understand. The nitroglycerin should": {
      "start_time": 134.94,
      "end_time": 140.76
    },
    "start working within minutes and if it doesnt fully relieve the pain, well": {
      "start_time": 140.76,
      "end_time": 144.04
    },
    "give you another dose or adjust your treatment accordingly.": {
      "start_time": 144.04,
      "end_time": 146.1
    },
    "Right now, the key is to keep you comfortable and stable.": {
      "start_time": 146.64,
      "end_time": 148.92
    },
    "Well also monitor your ECG continuously to make sure there are no further changes.": {
      "start_time": 149.28,
      "end_time": 152.56
    },
    "Ill get the orders in for the blood work and chest X-ray": {
      "start_time": 153.34,
      "end_time": 155.66
    },
    "and well also get Robin connected to the heart monitor.": {
      "start_time": 155.66,
      "end_time": 157.94
    },
    "Thank you, doctor.": {
      "start_time": 158.44,
      "end_time": 159.02
    }
}

#from emr get first visit of the patient, for every speciality, for every doctor.
def get_patient_type(patient_first_visit_date, current_visit_date):
    patient_first_visit_date = {
            "patient_id" : "",
            "speciality" : "",
            # "doctor_id" : "",
            "first_visit_date" : ""
        }

    if patient_first_visit_date["first_visit_date"] + timedelta(days=3*365)> current_visit_date:
        print("established patient")
        return "established"
    else:
        return "new"

def get_time_from_transcript(transcript):
    first_key = next(iter(transcript))
    first_value = transcript[first_key]
    ftof_start =first_value["start_time"]
    stof_end = first_value["end_time"]

    #face 2 face time
    for text, timings in transcript.items():
        start_time = timings["start_time"]
        end_time = timings["end_time"]
        if start_time < ftof_start:
            ftof_start = start_time
        if end_time > stof_end:
            stof_end = end_time
        # print(f"Text: {text}\nStart Time: {start_time}\nEnd Time: {end_time}\n")
    
    ftof_total = stof_end - ftof_start
    return ftof_total

def cpt_opd_EM_time_based(input):
    transcript = input["time_stamp_df"]
    patient_type = input["patient_type"]
    pdf_upload_time = input["pdf_upload_time"] if 'pdf_upload_time' in input else 0
    pdf_submit_time = input["pdf_submit_time"] if 'pdf_submit_time' in input else 0
    review_time = pdf_submit_time - pdf_upload_time
    #time components
    #review lab result
    ftof_total = get_time_from_transcript(transcript)
    ftof_total_min = ftof_total/60
    review_time_min = review_time/60
    total_time_min = ftof_total_min + review_time_min #in seconds

    cpt_code_reasoning = f""" The patient is {patient_type}, Doctor spent {review_time_min} minutes in reviewing lab data and took {ftof_total_min} for face to face encounter with the patient."""

    cpt_code = ""
    # get the code
    if patient_type == 'new':
        if total_time_min < 15:
            pass
        elif total_time_min >= 15 and total_time_min<30:
            cpt_code = "99202"
        elif total_time_min >= 30 and total_time_min<45:
            cpt_code = "99203"
        elif total_time_min >= 45 and total_time_min<50:
            cpt_code = "99204"
        elif total_time_min >=50 and total_time_min<75:
            cpt_code = "99205"
        else:
            cpt_code = "99205,99417"

    elif patient_type == 'established':
        if total_time_min < 10:
            pass
        elif total_time_min >= 10 and total_time_min<20:
            cpt_code = "99212"
        elif total_time_min >= 20 and total_time_min<30:
            cpt_code = "99213"
        elif total_time_min >= 30 and total_time_min<40:
            cpt_code = "99214"
        elif total_time_min >=40 and total_time_min<55:
            cpt_code = "99215"
        else:
            cpt_code = "99215,99417"
    else:
        cpt_code =""

    return cpt_code


def prolonged_obs_care(aggregated_time, section_max_time):
   extra_time = aggregated_time - (section_max_time+75)
   half_hour_splits = extra_time/30
   extra_add_on = ""
   for i in range(half_hour_splits):
       extra_add_on += "99357 "  
   return extra_add_on   

def is_same_day(date1, date2):
    return date1 == date2

# service_number in ["initial", "susequent", "discharge"]
def cpt_ipd_EM_time_based(input):
    # patient_id, aggregated_time, reasoniong, patient_type, care_type
    transcript = input["time_stamp_df"]
    pdf_upload_time = input["pdf_upload_time"] if 'pdf_upload_time' in input else 0
    pdf_submit_time = input["pdf_submit_time"] if 'pdf_submit_time' in input else 0
    f_to_f_time =  get_time_from_transcript(transcript)
    aggregated_time = f_to_f_time + pdf_submit_time - pdf_upload_time


    cpt_code = ""
    # get the code

    if data["service_setting"] == "ipd admission and discharge":
        if aggregated_time<45:
            cpt_code = "99234"
        elif aggregated_time<60:
            cpt_code = "99235"
        elif aggregated_time<85:
            cpt_code = "99236"
        elif  aggregated_time<(85+30): # for prolonged service, we have code only for time beyond 30 minutes
            cpt_code = "99236"
        elif aggregated_time < (85+75):
            cpt_code = "99236 99356"
        else:
            cpt_code = "99236 99356"
            extra_add_on = prolonged_obs_care(aggregated_time, 85)
            cpt_code = cpt_code + extra_add_on

    elif data["service_setting"] in ["ipd consultation","observation consultation"]:
        if aggregated_time<35:
            cpt_code = "99252"
        elif aggregated_time<40:
            cpt_code = "99253"
        elif aggregated_time<65:
            cpt_code = "99254"
        elif  aggregated_time<(65+30): # for prolonged service, we have code only for time beyond 30 minutes
            cpt_code = "99255"
        elif aggregated_time < (65+75):
            cpt_code = "99255 99356"
        else:
            cpt_code = "99255 99356"
            extra_add_on = prolonged_obs_care(aggregated_time, 65)
            cpt_code = cpt_code + extra_add_on

    elif data["service_setting"] in ["nursing"]:
        if "service_number" in input:
            service_number = input["service_number"]
            if service_number == "initial":
                if aggregated_time<25:
                    cpt_code = "99304"
                elif aggregated_time<35:
                    cpt_code = "99305"
                elif aggregated_time<50:
                    cpt_code = "99306"
                elif  aggregated_time<(50+30): # for prolonged service, we have code only for time beyond 30 minutes
                    cpt_code = "99306"
                elif aggregated_time < (50+75):
                    cpt_code = "99306 99356"
                else:
                    cpt_code = "99306 99356"
                    extra_add_on = prolonged_obs_care(aggregated_time, 50)
                    cpt_code = cpt_code + extra_add_on

            if service_number == "subsequent":
                if aggregated_time<10:
                    cpt_code = "99307"
                elif aggregated_time<20:
                    cpt_code = "99308"
                elif aggregated_time<30:
                    cpt_code = "99309"
                elif aggregated_time<45:
                    cpt_code = "99310"
                elif  aggregated_time<(45+30): # for prolonged service, we have code only for time beyond 30 minutes
                    cpt_code = "99310"
                elif aggregated_time < (45+75):
                    cpt_code = "99310 99356"
                else:
                    cpt_code = "99310 99356"
                    extra_add_on = prolonged_obs_care(aggregated_time, 45)
                    cpt_code = cpt_code + extra_add_on
    elif data["service_setting"] in ["residence"]:
        if "patient_type" in input and input["patient_type"] == "new":
            if aggregated_time<15:
                cpt_code = "99341"
            elif aggregated_time<30:
                cpt_code = "99342"
            elif aggregated_time<60:
                cpt_code = "99344"
            elif aggregated_time<75:
                cpt_code = "99345"
            elif  aggregated_time<(75+30): # for prolonged service, we have code only for time beyond 30 minutes
                cpt_code = "99345"
            elif aggregated_time < (75+75):
                cpt_code = "99345 99356"
            else:
                cpt_code = "99345 99356"
                extra_add_on = prolonged_obs_care(aggregated_time, 75)
                cpt_code = cpt_code + extra_add_on
        else:
            if aggregated_time<20:
                cpt_code = "99347"
            elif aggregated_time<30:
                cpt_code = "99348"
            elif aggregated_time<40:
                cpt_code = "99349"
            elif  aggregated_time<(60+30): # for prolonged service, we have code only for time beyond 30 minutes
                cpt_code = "99350"
            elif aggregated_time < (60+75):
                cpt_code = "99350 99356"
            else:
                cpt_code = "99350 99356"
                extra_add_on = prolonged_obs_care(aggregated_time, 60)
                cpt_code = cpt_code + extra_add_on

    elif "service_number" in input:
        service_number = input["service_number"]
        if service_number == "initial":
            if aggregated_time<40:
                cpt_code = "99221"
            elif aggregated_time<55:
                cpt_code = "99222"
            elif aggregated_time<75:
                cpt_code = "99223"
            elif  aggregated_time<(75+30): # for prolonged service, we have code only for time beyond 30 minutes
                cpt_code = "99223"
            elif aggregated_time < (75+75):
                cpt_code = "99223 99356"
            else:
                cpt_code = "99223 99356"
                extra_add_on = prolonged_obs_care(aggregated_time, 75)
                cpt_code = cpt_code + extra_add_on

        elif service_number == "subsequent":
            if aggregated_time<25:
                cpt_code = "99231"
            elif aggregated_time<35:
                cpt_code = "99232"
            elif aggregated_time<50:
                cpt_code = "99233"
            elif  aggregated_time<(50+30): # for prolonged service, we have code only for time beyond 30 minutes
                cpt_code = "99233"
            elif aggregated_time < (50+75):
                cpt_code = "99233 99356"
            else:
                cpt_code = "99233 99356"
                extra_add_on = prolonged_obs_care(aggregated_time, 50)
                cpt_code = cpt_code + extra_add_on

        elif service_number == "discharge":
            if aggregated_time<30:
                cpt_code = "99238"
            else:
                cpt_code = "99239"

    return cpt_code

def cpt_time_driver(input):
    cpt_code = ""
    if "service_setting" not in data:
        return False
    if data["service_setting"] in ["office", "other opd"] and "patient_type" in data:
        cpt_code = cpt_opd_EM_time_based(input)
    if data["service_setting"] in ["ipd", "observation care","ipd admission and discharge","ipd consultation","observation consultation", "nursing", "residence"]:
        cpt_code = cpt_ipd_EM_time_based(input)
    return cpt_code

transcription = """I have been having severe chest pain for the last few hours. It's not going away and it's really scaring me.
                    I understand Robin. Let's take it step by step. Can you describe the pain in more detail? Is it constant or does it come and go?
                    It's been constant and it feels like a heavy pressure. It started a few hours ago and it hasn't let up since. It's hard to catch my breath sometimes.
                    Alright. Any pain when I press on your chest? Or any sharp pain when you breathe in deeply?
                    No, not really. The pressure is inside, not on the surface.
                    I am not hearing any murmurs in your heart and your lungs sound clear which is a good sign.
                    But chest pain like this, especially with the obvious tree of hypertension, needs to be taken very seriously.
                    We need to rule out any heart related causes or the serious conditions. Doctor, her blood pressure is 160 over 100, heart rate is 110 and oxygen
                    saturation is 94%. Here's the ECG report we just ran. We also set up the IV. No
                    past history of heart issues but she's on amlodipine for hypertension and she
                    just started tolicity for her diabetes. Thanks. Hmm, Robin, it looks like there's
                    something showing up here. You see this part of the ECG, the ST segment? It's slightly depressed, which can sometimes indicate reduced blood flow to the heart.
                    This pattern is typical in angina, where the heart isn't receiving enough blood supply, especially during times of stress.
                    Angina? So it's not a heart attack?
                    Right now it looks more like angina than a full blown heart attack, which is a good thing.
                    Angina means that your heart isn't getting enough blood flow but it's not causing permanent
                    damage like a heart attack would.
                    Still, we need to act quickly to prevent anything from escalating.
                    So what happens next?
                    First I'm ordering cardiac enzyme tests through blood work.
                    This will help us confirm that there's no ongoing damage to your heart.
                    We'll also do a chest x-ray to rule out any lung issues that could be contributing to the pain.
                    I am continuing your current medication but I am going to give you oral nitroglycerin immediately.
                    It will help relieve the chest pain by dilating your blood vessels and allowing more blood to flow to your heart.
                    I will administer the nitroglycerin now doctor.
                    Am I going to be okay doctor?
                    Robin, we are taking all the necessary steps to make sure you are stable.
                    Angina is manageable but it is important to keep you monitored here for the next few days.
                    We'll run the tests, get the results and adjust your treatments as needed.
                    The good news is that we've caught this early, so we can take action before it becomes more serious.
                    That's reassuring. I just want this pain to go away.
                    I understand. The nitroglycerin should start working within minutes.
                    And if it doesn't fully relieve the pain, we'll give you another dose or adjust your treatment accordingly.
                    Right now, the key is to keep you comfortable and stable.
                    We'll also monitor your ECG continuously to make sure there are no further changes.
                    I'll get the orders in for the blood work and chest x-ray and we'll also get Robin connected to the heart monitor.
                    Thank you, doctor.
                    """
service_setting = ["office", "other opd", "ipd", "observation care", "ipd admission and discharge", \
                   "ipd consultation","observation consultation", "emergency", "nursing", "residence"], 

data = {
    "transcription":transcription,
    "time_stamp_df" : transcript,
    "physician_time":50, #time in minutes 
    "patient_type" :  "established",
    "service_setting": "ipd",
    "service_number" : "initial"
}

data = {
   "transcription":transcription,
   "time_stamp_df" : transcript,
   "physician_time":50, #time in minutes
   "patient_type" :  "established", #["new", "established"]
   "service_setting": "ipd", #["office", "other opd", "ipd", "observation care", "ipd admission and discharge", "ipd consultation","observation consultation", "emergency", "nursing", "residence"]
   "service_number" : "initial" #["initial", "subsequent", "discharge"]
}


print(cpt_time_driver(input))
# (code, reasoning) = cpt_opd_EM_time_based(transcript, 0, 200,"new")
# print("cpt_code: ", code, "\nreasoning : ", reasoning)