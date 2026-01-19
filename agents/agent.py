import os
import cohere
import re
from dotenv import load_dotenv
from .context import PROMPT

load_dotenv()

class QuestionParser:
    def __init__(self, queries):
        self.queries = queries

    def parse_question(self, question):
        if re.search(r"país.*huella|contamina", question, re.IGNORECASE):
            return self.queries.get_top_carbon_country()
        elif re.search(r"material.*utilizado", question, re.IGNORECASE):
            return self.queries.get_most_used_material()
        elif re.search(r"marca.*sostenible", question, re.IGNORECASE):
            return self.queries.get_most_sustainable_brand()
        else:
            return "Lo siento, no entiendo la pregunta."

class CohereAgent:
    def __init__(self, model_name="command-a-03-2025", queries=None):
        self.client = cohere.ClientV2(os.getenv("COHERE_API_KEY"))
        self.model_name = model_name
        self.system_prompt = PROMPT
        self.parser = QuestionParser(queries)

    def chat_with_history(self, message: str, chat_history=None):
        if chat_history is None:
            chat_history = []

        response_text = self.parser.parse_question(message)

        if response_text == "Lo siento, no entiendo la pregunta.":
            messages = [{"role": "system", "content": self.system_prompt}]
            messages.extend(chat_history)
            messages.append({"role": "user", "content": message})

            response = self.client.chat(
                model=self.model_name,
                messages=messages
            )
            response_text = response.message.content[0].text

        return response_text
