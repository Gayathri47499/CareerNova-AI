import streamlit as st


def hero_dashboard(user_name):

    st.markdown(

f"""
<div style="
padding:35px;
border-radius:22px;
background:linear-gradient(135deg,#1E3A8A,#2563EB);
color:white;
margin-bottom:25px;
">

<h1>
🚀 Welcome back,
{user_name}
</h1>

<p style="font-size:18px;opacity:.9;">

Your AI Career Coach is ready.

Continue building your dream career today.

</p>

</div>
""",

unsafe_allow_html=True
)
    