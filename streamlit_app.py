import streamlit as st

st.set_page_config(
    page_title="Minimarket ALTES",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 MINIMARKET ALTES")

st.subheader("Sistema de gestión del minimarket")

st.success("¡La aplicación se está ejecutando correctamente!")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sistema", "Activo")

with col2:
    st.metric("Aplicación", "Streamlit")

with col3:
    st.metric("Versión", "Inicial")

st.info(
    "Bienvenido a Minimarket ALTES. "
    "Estamos preparando la integración de los módulos existentes."
)