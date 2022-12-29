import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import time

st.set_page_config(
    page_title="Stata",
    page_icon="👋",
)

# uploading data
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

data = st.file_uploader("Wskaż położenie pliku CSV", type=['csv'])
if data is not None:
    with  st.spinner("Czekam..."):
        time.sleep(2)
    df = pd.read_csv(data)
    st.success("sukces!")
else:
    st.error("brak pliku")

    # st.dataframe(df.head(10))
if data is not None:
    # # select box
    wykres = st.selectbox("Twoja analiza", ("Wykres1", "Wykres2"))
    st.write("Zaprezentowany  : ", wykres)

    if wykres=="Wykres1":
        # # Plot
        st.success("Area chart")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        plot_data = df[selected_column_names]
        st.area_chart(plot_data)

    if wykres=="Wykres2":
        # # Plot
        st.success("Wykres liniowy")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        plot_data = df[selected_column_names]
        st.line_chart(plot_data)



# plot_dataNN = df[selected_column_names].plot(kind='box')
# st.write(plot_dataNN)
# st.pyplot()

# # dataframe
# st.dataframe(df)

# # tables
# st.table(df)