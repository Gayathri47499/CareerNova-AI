import streamlit as st


def status_badge(

    text,

    status="success"

):

    colors={

        "success":"#22C55E",

        "warning":"#F59E0B",

        "danger":"#EF4444",

        "info":"#3B82F6"

    }

    st.markdown(

f"""

<span style="

background:{colors[status]};

padding:6px 12px;

border-radius:20px;

color:white;

font-size:12px;

font-weight:bold;

">

{text}

</span>

""",

unsafe_allow_html=True

)