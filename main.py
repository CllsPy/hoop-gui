import streamlit as st

st.title("Hoop Web App")

col1, col2 = st.columns(2)

# Tipo de análise
tipo_analise = col1.radio(
	'selecione o tipo de análise', 
	["mecânica","condutividade"]
)


# Modelo
tipo_analise = col2.multiselect(
	'modelos', 
	["voigt","reuss"]
)
