import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def get_completion(client, question):
    return client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "system",
                "content": f"""
                    Você é um assistente técnico de terminal, especializado em responder dúvidas sobre programação, comandos de sistema, ferramentas de desenvolvedor e tecnologia em geral.
                    Responda de forma direta, objetiva e precisa à seguinte pergunta:
                    {question}
                    """
            }
        ],
        temperature=0.7,
        max_completion_tokens=150,
        top_p=0.95,
        stream=True,
        stop=None,
    )
