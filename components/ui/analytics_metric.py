import streamlit as st


def analytics_metric(

    title,

    value

):

    st.metric(

        title,

        f"{value}%"

    )