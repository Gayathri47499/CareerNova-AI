import streamlit as st


def stat_card(title, value, delta="", help_text=""):

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )