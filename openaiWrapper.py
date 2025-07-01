import os
from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_embeddings(texts, model=MODEL_NAME):
    response = openai_client.embeddings.create(input=texts, model=model)
    embeddings = [item.embedding for item in response.data]
    return embeddings

def gpt_summarize_and_categorize(case_description, model="gpt-3.5-turbo"):
    prompt = f"""
    Given the following medical case description, please:
    1. Provide a concise summary of the case.
    2. Categorize the information into the following sections if present: 'Evaluation and Management', and 'Other'.
    Return your response as a JSON object with keys: 'summary', 'evaluation and management', and 'other'.
    
    Case Description:
    {case_description}
    """
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful medical assistant."},
                  {"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content
    return content

def gpt_mdm_problem(transcription, summary, schema):
    first_prompt = """You are a highly skilled AI trained in language comprehension and identification. You will be provided with Transcript of a patient doctor conversation.
    You have to generate json as provided answering the quetions mention ed in it. You can take definitions for each term as will be mentioned below and use them to answer the questions.
    term definitions: 
    1. Minimal problem : problem that may not require the or other qualified health care professional, but the service is provided under the physician's or other qualified health care professional's supervision.
    2. Self-limited or minor problems: problem that runs a definite and prescribed course, is transient in nature, and is not likely to permanently alter health status.
    3. Stable, chronic illness: A problem with an expected duration of atleast one year or until the death of the patient. For the purpose of defining chronicity, conditions are treated as chronic whether or not stage or severity changes (eg, uncontrolled diabetes and controlled diabetes area single chronic condition). "Stable" for the purposes ofcategorizing MDM is defined by the specific treatment goals for an individual patient.A patient who is not at his or her treatment goal is not stable, even if the condition has not changed and there is no short-term threat to life or function. For example, a patient with persistently poorly controlled blood pressure for whom better control is a goal is not stable, even if the pressures are not changing and the patient is asymptomatic. The risk of morbidity without treatment is significant.
    4. Acute, uncomplicated illness or inJury: A recent or new short-term problem with low risk of morbidity for which treatment is considered. There is little to no risk of mortality with treatment, and full recovery without functional impairment is expected. A problem that is normally self-limited or minor but is not resolving consistent with a definite and prescribed course is an acute, uncomplicated illness.
    5. Acute uncomplicated illness or injury requiring hospital inpatient or observation level care : recent or new short-term problem with low risk of morbidity for which treatment is required. There is little to no risk of mortality with treatment, and full recovery without functional impairment is expected. The treatment required is delivered in a hospital inpatient or observation level setting.
    6. Stable, acute illness:A problem that is new or recent for which treatment has been initiated. The patient is improved and, while resolution may not be complete, is stable with respect to this condition.
    7. Chronic illness with exacerbation, progression or side effects of treatment: A chronic illness that is acutely worsening, poorly controlled, or progressing with an intent to control progression and requiring additional supportive care or requiring attention to treatment for side effects.
    8. Undiagnosed new problem with uncertain prognosis: A problem in the differential diagnosis that represents a condition likely to result in a high risk of morbidity without treatment.
    9. Acute illness with systemic symptoms: An illness that causes systemic symptoms and has a high risk of morbidity without treatment. For systemic general symptoms, such as fever, bodyaches, or fatigue in a minor illness that may be treated to alleviate symptoms, Systemic symptoms may not be general but may be single system.
    10. Acute complicated injury: An injury which requires treatment that includes evaluation of body systems that are not directly part of the injured organ, the injury is extensive, or the treatment options are multiple and/or associated with risk of morbidity.
    11. Chronic illness with severe exacerbation, progression or side effects of treatment: The severe exacerbation or progression ofa chronic illness or severe side effects of treatment that have significant risk of morbidity and may require escalation in level of care.
    12. Acute or chronic illness or injury that poses a threat to life or bodily function: A:n acute illness withsystemic symptoms, anacute complicated injury, ora chronic illness or injury with exacerbation and/or progression or side effects of treatment, that poses a threat to life or bodily function in the near term without treatment. Some symptoms may represent a condition that is significantly probable and poses a potential threat to life or bodily function. These may be included in this category when the evaluation and treatment are consistent with this degree of potential severity
    """
    transcript = "Following is the doctor patient convrsation : " + transcription
    first_prompt += transcript
    summary_prompt = "Following is the summary of the doctor patient consultation : " + summary
    first_prompt += summary_prompt
    return gpt_json_query(first_prompt, schema)

def gpt_mdm_data(transcription, summary, schema):
    first_prompt = """You are a highly skilled AI trained in language comprehension and identification. You will be provided with Transcript of a patient doctor conversation.
    You have to generate json as provided answering the quetions mention ed in it. You can take definitions for each term as will be mentioned below and use them to answer the questions.
    term definitions: ... (see cpt_mdm_data for full text) ..."""
    transcript = "Following is the doctor patient convrsation : " + transcription
    first_prompt += transcript
    summary_prompt = "Following is the summary of the doctor patient consultation : " + summary
    first_prompt += summary_prompt
    return gpt_json_query(first_prompt, schema)

def gpt_mdm_morbidity(transcription, summary, schema):
    first_prompt = """You are a highly skilled AI trained in language comprehension and identification. You will be provided with Transcript of a patient doctor conversation.
    You have to generate json as provided answering the quetions mention ed in it. You can take definitions for each term as will be mentioned below and use them to answer the questions.
    term definitions: ... (see cpt_mdm_morbidity for full text) ..."""
    transcript = "Following is the doctor patient convrsation : " + transcription
    first_prompt += transcript
    summary_prompt = "Following is the summary of the doctor patient consultation : " + summary
    first_prompt += summary_prompt
    return gpt_json_query(first_prompt, schema)

def gpt_make_reasoning_concise(reasoning, schema):
    first_prompt = " You are an highly skilled language model. following is a reasoning for a cpt code. By retaining all the important informations make this reasoning brief. Remove sentneces which does not carry information. The output should be in the json schema as given. Keep the reason in less than 100 words"
    return gpt_json_query(first_prompt + "\n" + reasoning, schema)

def gpt_json_query(prompt, schema, model="gpt-4o-2024-08-06"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        presence_penalty=0.1,
        seed=413,
        response_format=schema
    )
    return response.choices[0].message.content
