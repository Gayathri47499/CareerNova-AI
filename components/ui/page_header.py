import streamlit as st


def page_header(

    title,

    subtitle,

    icon="🚀"

):

    st.markdown(

f"""

# {icon} {title}

<span style="color:#94A3B8;font-size:18px;">

{subtitle}

</span>

""",

unsafe_allow_html=True

)

st.divider()