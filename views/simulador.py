import streamlit as st
from models.credit import CreditoHipotecario, CreditoVehicular
from controllers.credit_controller import CreditController

controlador = CreditController()

def mostrar():
    st.title("Simulador de Créditos")

    tipo = st.selectbox("Tipo de crédito", ["Hipotecario", "Vehicular"])
    monto = st.number_input("Monto de crédito", min_value=1000, step=1000)
    plazo = st.slider("Plazo (años)", 1, 30)
    tasa = st.number_input("Tasa de interés (%)", min_value=0.1, step=0.1)

    if st.button("Calcular cuota"):
        if tipo == "Hipotecario":
            credito = CreditoHipotecario(monto, plazo, tasa)
        else:
            credito = CreditoVehicular(monto, plazo, tasa)
        
        cuota = credito.calcular_cuota()
        st.success(f"La cuota mensual es: S/. {cuota}")
        controlador.guardar({
            "tipo": tipo,
            "monto": monto,
            "plazo": plazo,
            "tasa": tasa,
            "cuota": cuota
        })