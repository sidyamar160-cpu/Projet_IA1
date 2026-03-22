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

st.subheader("Ventes totales par produit")

totaux = data_filtre[produits].sum()

fig1, ax1 = plt.subplots()
totaux.plot(kind='bar', ax=ax1)
plt.title("Total des ventes")
st.pyplot(fig1)


st.subheader("Comparaison des ventes par canal")

par_canal = data_filtre.groupby("Channel")[produits].sum()

fig2, ax2 = plt.subplots()
par_canal.plot(kind='bar', ax=ax2)
plt.title("Ventes par canal")
st.pyplot(fig2)


st.subheader("Comparaison des ventes par région")

par_region = data_filtre.groupby("Region")[produits].sum()

fig3, ax3 = plt.subplots()
par_region.plot(kind='bar', ax=ax3)
plt.title("Ventes par région")
st.pyplot(fig3)


st.subheader("Corrélation entre les produits")

fig4, ax4 = plt.subplots()
sns.heatmap(data_filtre[produits].corr(), annot=True, cmap="coolwarm", ax=ax4)
st.pyplot(fig4)


st.subheader("Relations entre les variables")

fig5 = plt.figure()
scatter_matrix(data_filtre[produits], figsize=(10,10))
st.pyplot(fig5)


st.subheader("Analyse automatique")

produit_max = totaux.idxmax()
produit_min = totaux.idxmin()

st.write(f"Produit le plus vendu : **{produit_max}**")
st.write(f"Produit le moins vendu : **{produit_min}**")

canal_max = data_filtre.groupby("Channel")[produits].sum().sum(axis=1).idxmax()
region_max = data_filtre.groupby("Region")[produits].sum().sum(axis=1).idxmax()

st.write(f"Canal le plus performant : **{canal_max}**")
st.write(f"Région la plus performante : **{region_max}**")




