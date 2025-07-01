
from openai import OpenAI
import json


def GetMessageMemory(openai_client, NewQuestion, lastmessage, json_structure = {}):
    # Append the new question to the last message
    lastmessage.append({"role": "user", "content": NewQuestion})

    # msgcompletion = openai_client.chat.completions.create(
    #     messages=lastmessage,
    #     # model="gpt-4o-2024-08-06",
    #     model="o1-preview-2024-09-12"
    #     # temperature=0.0,
    #     # presence_penalty=0.1,
    #     # seed=413,
    #     # response_format=json_structure
    # )
    msgcompletion = openai_client.chat.completions.create(
        messages=lastmessage,
        model="gpt-4o-2024-08-06",
        # model="o1-preview-2024-09-12"
        temperature=0.0,
        presence_penalty=0.1,
        seed=413,
        # response_format=json_structure
    )
    msgresponse = msgcompletion.choices[0].message.content
    return msgresponse

def cpt_modifiers(openai_client, transcription, summary ):
    first_prompt = """You are a highly skilled AI trained in language comprehension and identification. You will be provided with Transcript of a patient doctor conversation."""
    
    transcript = "Following is the doctor patient convrsation : "+ transcription
    first_prompt += transcript
    summary_prompt = "Following is the summary of the doctor patient consultation : "+ summary
    first_prompt += summary_prompt

    final_query = """
        consuming the above information generate the following object by answering the questions mentioned in it. Answer will be yes or no. Explanation will should contain why that answer has that value. 
        {
            "section" : "data reviewed",
            questions: {
                1: {
                "id" : 1,
                "question" : "Is the patient in a post operative care?"
                "answer":"",
                "explanation":"",
                "modifier" : "24"

                },
                 2: {
                "id" : 2,
                "question" : "is this visit Unrelated Evaluation and Management Service by the Same Physician or Other Qualified Health Care Professional During a Postoperative period?"
                "answer":"",
                "explanation":"",
                "modifier" : "24"

                },
                3: {
                "id" : 3,
                "question" : ""
                "answer":"",
                "explanation":""
                },

                4: {
                "id" : 4,
                "question" : "Is there Significant, Separately Identifiable Evaluation and Management Service by the Same Physician or Other Qualified Health Care Professional on the Same Day of the Procedure or Other Service"
                "answer":"",
                "explanation":"",
                "modifier" : "25"
                },

                5: {
                "id" : 5,
                "question" : "If a procdure is done, is the service performed during a postoperative period if related to the previous surgery"
                "answer":"",
                "explanation":"",
                "modifier" : "25"

                },

                6:{
                "id" : 6,
                "question" : "Is the visit mandated by a third party? example : Often used for services like second opinions, consultative exams, or evaluations required by worker’s compensation, court orders, or insurance requests"
                "answer":"",
                "explanation":"",
                "modifier" : "32"

                },
                7:{
                "id" : 7,
                "question" : "Did this visit resulted in a decision to conduct a surgery?"
                "answer":"",
                "explanation":"",
                "modifier" : "57"
                },

                8:{
                "id" : 8,
                "question" : "was this consultation Habilitative? Habilitative means services help an individual learn skills and functioning for
daily living that the individual has not yet developed, and
then keep and/or improve those learned skills. Habilitative
services also help an individual keep, learn, or improve skills
iind functioning fordaily livinig."
                "answer":"",
                "explanation":"96"
                },

                9:{
                "id" : 9,
                "question" : "was this consultation Rehabilitative? Rehabilitative Rehabilicative services help an individual keep, get back, or improve skills and functioning for daily living that have 
been lost or impaired because the individual was sick, hurt, 
or disabled."
                "answer":"",
                "explanation":"97"
                },

                10:{
                "id" : 10,
                "question" : "Is the service provided is preventive care?"
                "answer":"",
                "explanation":"",
                "modifier" : "33"
                }
            }
        }
    """

    last_message_list = [{"role": "user", "content": first_prompt}]
    json_data_str = GetMessageMemory(openai_client, final_query, last_message_list) 
    # json_data = json.loads(json_data_str)
    print("data json : ", json_data_str)

    return


summary_8 ="""A new patient reports to the orthopedist complaining of pain and swelling in his right shoulder. The physician performs an E/M service, which includes a detailed history and examination, along with moderate medical decision making (MDM). After the E/M, the clinician diagnoses bicipital tendinitis of the right shoulder, and performs an arthrocentesis joint injection to reduce the swelling. There is no evidence of ultrasound guidance."""
"""services performed during a postoperative period if related to the previous surgery.
Do not append Modifier 25 if there is only an E/M service performed during the office visit (no procedure done).
Do not use a Modifier 25 on any E/M on the day a “Major” (90 day global) procedure is being performed.
Do not append Modifier 25 to an E/M service when a minimal procedure is performed on the same day unless the level of service can be supported as significant, separately identifiable. All procedures have an “inherent” E/M service included. See example #2.
Patient came in for a scheduled procedure only"""
data = {
    # "transcription":transcription_14,
    "summary" : summary_8,
    "patient_type" :  "new",
    "service_setting": "opd",
    "service_number" : "initial"
}
print(cpt_modifiers(openai_client, "", summary_8 ))