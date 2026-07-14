import streamlit as st


def progress_card(title, value):

    st.write(title)

    st.progress(value)