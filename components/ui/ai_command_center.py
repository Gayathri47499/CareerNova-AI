import streamlit as st


def ai_command_center():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#2563EB,#7C3AED);
        padding:28px;
        border-radius:18px;
        color:white;
        margin-top:20px;
        margin-bottom:20px;
        box-shadow:0px 12px 30px rgba(0,0,0,.25);
    ">

    <h2>🤖 AI Command Center</h2>

    <p>
    Ask CareerNova AI anything about your career.
    </p>

    </div>
    """, unsafe_allow_html=True)

    question = st.text_input(

        "",

        placeholder="Example: How can I become an AI Engineer at Google?"

    )

    analyze = st.button(

        "✨ Analyze with AI",

        use_container_width=True

    )

    return analyze, question