import streamlit as st


def recommendation_card(text):

    st.markdown(
        f"""
<div style="
background:#1E293B;
padding:20px;
border-radius:16px;
border-left:6px solid #3B82F6;
margin-top:15px;
">

<h4>🤖 AI Recommendation</h4>

<p>{text}</p>

</div>
""",
        unsafe_allow_html=True
    )