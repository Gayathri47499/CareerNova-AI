import streamlit as st


def explanation_card(title, items, success=True):

    color = "#22C55E" if success else "#EF4444"

    icon = "✅" if success else "❌"

    st.markdown(
        f"""
<div style="
background:#111827;
padding:20px;
border-radius:18px;
border-left:5px solid {color};
margin-bottom:20px;
">
<h3>{title}</h3>
</div>
""",
        unsafe_allow_html=True
    )

    for item in items:
        st.write(f"{icon} {item}")