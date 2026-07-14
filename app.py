import streamlit as st
from data.initialize_database import initialize_database

initialize_database()


# =====================================================
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# =====================================================

st.set_page_config(
    page_title="CareerNova AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

# =====================================================
# LOAD CSS
# =====================================================

def load_css():

    with open("assets/css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =====================================================
# LOGIN / REGISTER
# =====================================================

from views import login, register

if not st.session_state.logged_in:

    if st.session_state.current_page == "login":

        login.show()

    else:

        register.show()

    st.stop()

# =====================================================
# IMPORT AFTER LOGIN
# =====================================================

from components.sidebar import show_sidebar

from views import (
    dashboard,
    resume,
    ats,
    career,
    interview,
    analytics,
    chat,
    settings,
)

# =====================================================
# SIDEBAR
# =====================================================

page = show_sidebar()

# =====================================================
# ROUTING
# =====================================================

if page == "Dashboard":

    dashboard.show()

elif page == "Resume":

    resume.show()

elif page == "ATS":

    ats.show()

elif page == "Career":

    career.show()

elif page == "Interview":

    interview.show()

elif page == "Analytics":

    analytics.show()

elif page == "Chat":

    chat.show()

elif page == "Settings":

    settings.show()