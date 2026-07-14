import streamlit as st


def skill_chip(

    skill,

    color="#3B82F6"

):

    st.markdown(

f"""

<span style="

background:{color};

padding:8px 14px;

border-radius:999px;

color:white;

margin:5px;

display:inline-block;

font-size:13px;

font-weight:600;

">

{skill}

</span>

""",

unsafe_allow_html=True

)