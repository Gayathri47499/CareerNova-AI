import streamlit as st


def show_hero():

    st.markdown(
        """
        <div class="hero-card">

        <div class="hero-title">

        🚀 CareerNova AI

        </div>

        <div class="hero-subtitle">

        Your Personal AI Career Intelligence Platform

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )