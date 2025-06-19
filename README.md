# Sabetudo CLI

Um assistente de linha de comando (CLI) em Python que consulta a API de IA da Groq para responder perguntas diretamente do terminal.

## Pré‑requisitos

- Python 3.8 ou superior
- pip ou [pipx](https://pypa.github.io/pipx/)
- Conta na [Groq](https://console.groq.com/) e chave de API

## Instalação

Primeiro, clone este repositório:

```bash
git clone https://github.com/gabriel04alves/sabetudo-cli.git
cd sabetudo-cli
```

## Obter a API Key da Groq

1. Acesse o [painel da Groq](https://console.groq.com/).
2. Faça login ou crie uma conta.
3. No menu lateral, clique em **API Keys**.
4. Gere uma nova chave ou copie uma existente.
5. Exporte a chave como variável de ambiente:
   ```bash
   export GROQ_API_KEY="sua_chave_aqui"
   ```
   Ou crie um arquivo `.env` na raiz do projeto:
   ```
   GROQ_API_KEY=sua_chave_aqui
   ```

### Definindo a variável de ambiente permanentemente

Para não precisar exportar a variável toda vez que abrir o terminal, adicione a linha abaixo ao arquivo de configuração do seu shell:

- **Bash** (Ubuntu, Debian, Fedora, etc):
  ```bash
  echo 'export GROQ_API_KEY="sua_chave_aqui"' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Zsh** (macOS, algumas distros Linux):
  ```bash
  echo 'export GROQ_API_KEY="sua_chave_aqui"' >> ~/.zshrc
  source ~/.zshrc
  ```
- **Fish**:
  ```fish
  set -Ux GROQ_API_KEY "sua_chave_aqui"
  ```

Depois disso, a variável estará disponível sempre que abrir um novo terminal.

### Instalação em diferentes distribuições Linux

### Fedora

```bash
sudo dnf install python3 python3-pip
pip install --user .
```

### Debian/Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip
pip install --user .
```

### Arch/Manjaro

```bash
sudo pacman -S python python-pip
pip install --user .
```

## Instalação definitiva (global)

Você pode instalar o Sabetudo CLI globalmente com:

```bash
pip install .
# ou
pip install --user .
```

Verifique a instalação:

```bash
sabetudo --help
```

## Instalação e teste em ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install typer requests python-dotenv
# (instale também groq se necessário)
pip install .
python -m sabetudo "sua pergunta"
```

## Uso básico

Faça perguntas diretamente pelo terminal:

```bash
sabetudo "qual o comando para limpar o terminal?"
```

## Estrutura de Pastas

Árvore resumida do projeto:

```
sabetudo-cli/
├── src/
│   ├── app.py
│   ├── __init__.py
│   └── services/
│       └── client.py
├── .env.example
├── pyproject.toml
├── README.md
```

## Contribuição e Licença

Contribuições são bem-vindas! Abra issues ou envie pull requests.

Licença: MIT. Consulte o arquivo `LICENSE` para mais detalhes.
