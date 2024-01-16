import pandas as pd
import urllib.parse
import webbrowser
import streamlit as st

st.title('Hierarchical data viewer')

df = pd.read_csv('data/employees.csv', header=0).convert_dtypes()

st.dataframe(df)

edges = ''
for _, row in df.iterrows():
    emp_name = row.iloc[0]
    mgr_name = row.iloc[1]
    if not pd.isna(mgr_name):
        edges += f'\t"{emp_name}" -> "{mgr_name}";\n'

d = f'digraph {{\n{edges}}}'
st.graphviz_chart(d)

