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