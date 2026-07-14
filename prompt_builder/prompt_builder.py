import json


class PromptBuilder:

    def build(

        self,

        system_prompt,

        context,

        question

    ):

        prompt = f"""

{system_prompt}

==================================

Candidate Context

{json.dumps(context, indent=4)}

==================================

User Question

{question}

==================================

Give a professional answer.

"""

        return prompt