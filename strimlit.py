import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('Dataset.csv')


def fill_empties(matrix, value):

    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column].fillna(int(value), inplace=True)
    return df


max_value = df.max().max()
st.write('Max of second column:', max_value)

min_value = df.min().min()
st.write('Min of second column:', min_value)

selected_range = st.slider('', min_value, max_value)

if isinstance(selected_range, tuple):
    selected_min = selected_range[0]
    selected_max = selected_range[1]
else:
    selected_min = selected_range
    selected_max = selected_range

df = fill_empties(df, selected_max)

st.write(df)
