import streamlit as st


def activity_card(

    title,

    description,

    icon="✅"

):

    st.markdown(

f"""

<div style="

background:#1E293B;

padding:18px;

border-radius:14px;

margin-bottom:12px;

">

<b>{icon} {title}</b>

<br>

<span style="color:#94A3B8">

{description}

</span>

</div>

""",

unsafe_allow_html=True

)