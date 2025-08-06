import streamlit as st

def mostrar():
    st.title("Bienvenido al simulador Bancario")
    st.markdown("""
        Esta aplicación permite simular créditos hipotecarios o vehiculares.
        Próximamente se conectará con Supabase para guardar las simulaciones.
    """)