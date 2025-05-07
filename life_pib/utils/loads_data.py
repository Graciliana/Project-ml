import pandas as pd
import streamlit as st

# carregar os dados
oecd_bli = pd.read_csv(
    "https://raw.githubusercontent.com/ageron/handson-ml/refs/heads/master/datasets/lifesat/oecd_bli_2015.csv",
    thousands=",",
)
gdp_per_capita = pd.read_csv(
    "https://raw.githubusercontent.com/ageron/handson-ml/refs/heads/master/datasets/lifesat/gdp_per_capita.csv",
    thousands=",",
    delimiter="\t",
    encoding="latin1",
    na_values="n/a",
)
