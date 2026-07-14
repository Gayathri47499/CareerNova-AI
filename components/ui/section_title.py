import streamlit as st


def section_title(title, subtitle=""):

    st.markdown(f"## {title}")

    if subtitle:

        st.caption(subtitle)