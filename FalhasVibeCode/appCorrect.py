import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAi_Key"))

st.set_page_config(page_title="ShopAi", page_icon="🛍️")
st.title("🛍️ ShopAi")
st.caption("Seu assistente virtual de compras")

if "Mensagens" not in st.session_state:
    st.session_state["Mensagens"] = [
        {"role": "system", "content": "Você é o assistente virtual da ShopAi, uma loja online. Ajude os clientes com dúvidas sobre produtos, pedidos, entregas e trocas. Seja educado, objetivo e não invente informações sobre produtos ou pedidos."}
    ]

for mensagem in st.session_state["Mensagens"][1:]:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

if prompt := st.chat_input("Como posso ajudar você?"):
    st.session_state["Mensagens"].append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["Mensagens"]
        )
        texto = resposta.choices[0].message.content
        st.write(texto)

    st.session_state["Mensagens"].append(
        {"role": "assistant", "content": texto}
    )
