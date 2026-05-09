# 🐍 Hashtag - Intensivão de Python

Repositório com os projetos desenvolvidos durante o **Intensivão de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/).

## 📚 Aulas

| Aula | Conteúdo |
|------|----------|
| Aula 01 | Introdução ao Python |
| Aula 02 | — |
| Aula 03 | — |
| Aula 04 | Integração com OpenAI API + Streamlit |

> As descrições das aulas intermediárias podem ser atualizadas conforme o progresso do curso.

## 🚀 Como executar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/thiagomw/Hashtag-Jornada-Python.git
cd Hashtag-Jornada-Python
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env na raiz do projeto
cp .env.example .env
```

Edite o `.env` com sua chave da OpenAI:
```
OPENAI_API_KEY=sua-chave-aqui
```

4. Execute o projeto da aula desejada, por exemplo:
```bash
streamlit run "aula 04/main.py"
```

## 🔐 Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `OPENAI_API_KEY` | Chave de API da OpenAI |

> ⚠️ **Nunca commite o arquivo `.env` no repositório!** Ele já está no `.gitignore`.

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 📎 Links úteis

- [Evento Intensivão de Python - Hashtag](https://lp.hashtagtreinamentos.com/python/intensivao/blog?aula=1)
- [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/)
