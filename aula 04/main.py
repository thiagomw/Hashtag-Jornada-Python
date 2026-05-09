# Titulo
# Input do chat 
# A cada mensagem que o usuário enviar:
    # Mostrar a mensagem que o usuário enviou no chat
    # Pegar a perguntar e enviar para uma IA responder
    # Exibir a resposta da IA na tela
# Huggin Face - baixa e treina ele para o que a gente precisa. Se quiser criar o proprio modelo
# LangChain
# Systemprompt, oque a IA pode ou nao fazer, contexto, etc etc etc

import streamlit as st
import os
from openai import OpenAI
from openai import RateLimitError
from dotenv import load_dotenv

load_dotenv()

modelo_ia = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.write("# MURIDAE - Chatbot")
# arquivo = st.file_uploader("Selecione um arquivo")

if not "lista_mensagens" in st.session_state:
        st.session_state["lista_mensagens"] = []
        # st.session_state["lista_mensagens"] = [{"role": "system", "content": "Contexto de prompt inicial"}]

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)
    
texto_usuario = st.chat_input("Digite a sua mensagem")

if texto_usuario:
    st.chat_message("user").write(texto_usuario) #Nome: aparece a primeira letra do nome / #User: icone de usuário# #Assistant: icone da IA
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    try:
        resposta_ia = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-4o"
            )
            # IA Respondeu

        resposta_ia = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-4o"
        )

        texto_resposta_ia = resposta_ia.choices[0].message.content

        st.chat_message("assistant").write(texto_resposta_ia)
        mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)
        
    except RateLimitError:
        st.error("Limite de cota da OpenAI atingido. Verifique seu plano em platform.openai.com/billing")
        st.stop()