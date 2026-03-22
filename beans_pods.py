import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix




chemin = 'BeansDataSet.csv'
data = pd.read_csv(chemin)


st.sidebar.title("Analyse des ventes de Beans & Pods")

st.sidebar.header("Filtres")

chaines = st.sidebar.selectbox(
    "Choisissez le canal",
    ["Tous"] + list(data["Channel"].unique())
)

region = st.sidebar.selectbox(
    "Choisissez la région",
    ["Toutes"] + list(data["Region"].unique())
)

data_filtre = data.copy()

if chaines != "Tous":
    data_filtre = data_filtre[data_filtre["Channel"] == chaines]

if region != "Toutes":
    data_filtre = data_filtre[data_filtre["Region"] == region]


st.markdown("""
<div style='text-align: center;'>
<h1>Beans & Pods </h1>
<p style='color:red;'>Analyse interactive des ventes</p>
</div>
""", unsafe_allow_html=True)


st.subheader("Aperçu des données")
st.dataframe(data_filtre)

st.subheader("Statistiques descriptives")
st.write(data_filtre.describe())


produits = ["Robusta", "Arabica", "Espresso", "Lungo", "Latte", "Cappuccino"]
