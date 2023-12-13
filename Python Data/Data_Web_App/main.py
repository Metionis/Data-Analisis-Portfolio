import streamlit as st
import pandas as pd

st.write("""
# My First App
Hello *world!*         
""")

df = pd.read_csv("data\customer_booking.csv",  encoding="ISO-8859-1")
st.line_chart(df["purchase_lead"])