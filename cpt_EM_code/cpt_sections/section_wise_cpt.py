
def get_total_time(service_durations):
    total_time = 0
    for item in service_durations:
        if "time" in item:
            total_time += item["time"]
    return total_time

def critical_care_time_based(input):
#       CPT 99291: Critical care, first 30-74 minutes
#       CPT 99292: Each additional 30 minutes after the first 74 minutes
    #befor coming to this function make sure service_durations key is available in input

    total_time = get_total_time(input["service_durations"])  
    if total_time < 30:
        reason = "duration of critical care service is less than 30 mins, So no code"
        return False
    elif total_time <75:
        reason = "duration in less than 75 min hnec the follwoing code"
        return "99291"
    else:
        cpt_code = "99291"
        remaining_time = total_time - 75
        batches = remaining_time//30
        for i in range(batches):
            cpt_code += ",99291"
        return cpt_code


def psychotherapy_time_based(input):
# CPT 90832: Psychotherapy, 30 minutes with patient.
# CPT 90834: Psychotherapy, 45 minutes with patient.
# CPT 90837: Psychotherapy, 60 minutes with patient.
    
    total_time = get_total_time(input["service_durations"])  
    if total_time < 30:
        reason = "duration of psychotherapy service is less than 30 mins, So no code"
        return False
    elif total_time <45:
        reason = "duration in less than 75 min hnec the follwoing code"
        return "90832"
    elif total_time <60:
        reason = "duration in less than 75 min hnec the follwoing code"
        return "90834"
    else:
        cpt_code = "90837"
        # remaining_time = total_time - 75
        # batches = remaining_time//30
        # for i in range(batches):
        #     cpt_code += ",99291"
        return cpt_code