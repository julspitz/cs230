#streamlit run finalProject.py

import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pandas as pd
import numpy as np
import statistics

#title & header
st.title('Heart Disease Analysis Project')
st.header('Juliana, Gaby, Luke')
st.write(' ')
df = st.cache(pd.read_csv)("heart.csv")
st.write(df)

#Pivot Table
#User chooses whether they would like to view a pivot table of price or destination, showing Uber vs. Lyft rides for each source/destination combo
def pivot():
    values = st.radio("View Gender or Diabetic Data:", ('Sex', 'Diabetic'))
    pivTable = pd.pivot_table(df, values=values, index=['Sex', 'Diabetic'], columns='HeartDisease', aggfunc=np.sum)
    st.write(pivTable)
    pass
