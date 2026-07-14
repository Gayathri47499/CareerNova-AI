import streamlit as st


def glass_card(

    title,

    content,

    icon="✨"

):

    st.markdown(

        f"""

<div style="

background:rgba(255,255,255,0.05);

backdrop-filter:blur(14px);

border-radius:18px;

padding:25px;

margin-top:15px;

border:1px solid rgba(255,255,255,0.08);

box-shadow:0px 8px 30px rgba(0,0,0,0.25);

">

<h3>{icon} {title}</h3>

<p>{content}</p>

</div>

""",

unsafe_allow_html=True

)