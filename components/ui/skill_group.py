import streamlit as st


def skill_group(title, skills, color):

    st.subheader(title)

    if not skills:

        st.info("No skills")

        return

    html = ""

    for skill in skills:

        html += f"""
<span style="
background:{color};
padding:8px 14px;
margin:6px;
border-radius:999px;
display:inline-block;
color:white;
font-weight:600;
font-size:13px;
">
{skill}
</span>
"""

    st.markdown(html, unsafe_allow_html=True)