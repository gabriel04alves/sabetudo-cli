import os
import sys
import typer
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = typer.Typer()
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

@app.command()
def __call__(question):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.7,
            max_completion_tokens=150,
            top_p=0.95,
            stream=True,
            stop=None,
        )
        
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            typer.secho(content, nl=False)
        
        print()
        
    except Exception as e:
        typer.secho(f"Erro na requisição: {e}", fg=typer.colors.RED)
        sys.exit(1)

if __name__ == "__main__":
    app()