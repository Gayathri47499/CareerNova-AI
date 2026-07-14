import json

from models.resume_models import ResumeData

from agents.career_agent import CareerAgent


class ResumeExtractor:

    def __init__(self):

        self.ai = CareerAgent()

    def extract(self, resume_text):

        prompt = f"""
You are an expert AI Resume Intelligence Engine.

Analyze the resume carefully.

Return ONLY valid JSON.

Do not write explanations.

Do not use markdown.

Return exactly this structure:

{{
"name":"",
"email":"",
"phone":"",

"education":[
{{
"degree":"",
"field":"",
"university":"",
"duration":"",
"cgpa":""
}}
],

"skills":{{
"languages":[],
"backend":[],
"databases":[],
"cloud":[],
"ai_genai":[],
"tools":[]
}},

"projects":[
{{
"name":"",
"technologies":[],
"description":""
}}
],

"experience":[
{{
"role":"",
"duration":"",
"achievements":[]
}}
],

"certifications":[],

"career_profile":{{
"career_level":"",
"recommended_roles":[],
"technical_strengths":[],
"soft_skills":[],
"missing_skills":[]
}}

}}

Resume:

{resume_text}
"""

        response = self.ai.chat(prompt)

# Remove Markdown code fences
        response = response.strip()

        if response.startswith("```json"):
         response = response.replace("```json", "", 1)

        if response.endswith("```"):
         response = response[:-3]

        response = response.strip()

        data = json.loads(response)

        return ResumeData(**data)