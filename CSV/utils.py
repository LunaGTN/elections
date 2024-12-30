import streamlit as st
import pandas as pd


df_Legis_22_T1 = pd.read_csv('Legis_22_T1.csv')
df_legis_22_T2 = pd.read_csv('legis_22_T2.csv')
df_Legis_24_T1 = pd.read_csv('Legis_24_T1.csv')
df_legis_24_T2 = pd.read_csv('legis_24_T2.csv')
df_municipales_20_T1 = pd.read_csv('municipales_20_T1.csv')
df_municipales_20_T2 = pd.read_csv('municipales_20_T2.csv')
df_presidentielle_20_T1 = pd.read_csv('presidentielle_20_T1.csv')

st.title('Résultats des élections - Toulouse')

if st.button("TOULOUSE"):
    st.write("Résultats pour tout toulouse")

col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("Par quartier de Mairie", #colonnes quartiers de mairie
    ['Simba', 'Scar', 'Zazu'])
with col2:
    st.selectbox("Par quartiers",
    ['Simba', 'Scar', 'Zazu'])
with col3:
    st.selectbox("Par bureaux de vote",
    ['Simba', 'Scar', 'Zazu'])

