import streamlit as st


def skill_progress(title, score):

    st.write(title)

    st.progress(score / 100)

    st.caption(f"{score}%")