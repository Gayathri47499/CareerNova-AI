import streamlit as st


def dashboard_metric(

    icon,

    title,

    value,

    subtitle,

    color="#3B82F6"

):

    st.markdown(

f"""

<div style="

background:#111827;

padding:22px;

border-radius:18px;

border-left:6px solid {color};

box-shadow:0 6px 18px rgba(0,0,0,.25);

height:150px;

">

<div style="font-size:36px">

{icon}

</div>

<h4>{title}</h4>

<h2>{value}</h2>

<p style="color:#94A3B8">

{subtitle}

</p>

</div>

""",

unsafe_allow_html=True

)