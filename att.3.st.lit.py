import streamlit as st

st.title("faça seu login")
st.header("cadastro")

login_correto = "tcheca123"
senha_correta = "123"

login = st.text_input("digite seu login: ")
senha = st.text_input("digite seu senha: ")

if st.button("entrar"):
    if login == login_correto and senha == senha_correta:
        st.success("login com sucesso")
    else:
        st.error("login sem sucesso")
        1
                                 
