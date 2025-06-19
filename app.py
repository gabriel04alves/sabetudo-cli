import os
import sys
import typer
from dotenv import load_dotenv
from services.client import client, get_completion

load_dotenv()

app = typer.Typer()

@app.command()
def __call__(question):
    try:
        completion = get_completion(client, question)
        
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            typer.secho(content, nl=False)
        print()
        
    except Exception as e:
        typer.secho(f"Erro na requisição: {e}", fg=typer.colors.RED)
        sys.exit(1)

if __name__ == "__main__":
    app()