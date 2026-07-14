import streamlit as st


def health_card(score):

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
padding:25px;
border-radius:22px;
border:2px solid {color};
text-align:center;
">

<h2>
Career Health
</h2>

<h1 style="
font-size:70px;
color:{color};
">
{score}%
</h1>

<h3 style="
color:{color};
">
{status}
</h3>

</div>
""",

unsafe_allow_html=True
)