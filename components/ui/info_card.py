import streamlit as st


def info_card(title, message):

    st.info(

        f"**{title}**\n\n{message}"
    )