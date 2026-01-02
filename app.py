import streamlit as st
import pandas as pd
from src.ranker import rank_destinations, load_data

st.set_page_config(page_title="Weekend Getaway Ranker", layout="wide")

st.title("Weekend Getaway Ranker")

@st.cache_data
def load():
    return load_data("data/Top Indian Places to Visit.csv")

df = load()

cities = sorted(df['City'].unique())

source_city = st.selectbox("Select Source City", cities)

top_n = st.slider("Number of Recommendations", 3, 10, 5)

if st.button("Find Getaways"):
    results = rank_destinations(df, source_city, top_n)
    st.dataframe(results)
