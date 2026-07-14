import streamlit as st


def hero_score(score):

    if score >= 85:
        color = "#22C55E"
        status = "Excellent"

    elif score >= 70:
        color = "#F59E0B"
        status = "Good"

    else:
        color = "#EF4444"
        status = "Needs Improvement"

    st.markdown(
        f"""
<div style="
background:#111827;
padding:35px;
border-radius:20px;
text-align:center;
border:2px solid {color};
box-shadow:0px 8px 25px rgba(0,0,0,.25);
">

<h3 style="color:white;">🎯 ATS Score</h3>

<h1 style="font-size:70px;color:{color};margin:0;">
{score}%
</h1>

<p style="color:{color};font-size:22px;font-weight:bold;">
{status}
</p>

</div>
""",
        unsafe_allow_html=True
    )