import streamlit as st


def show_dashboard_cards():

    col1,col2,col3,col4 = st.columns(4)

    with col1:

        st.metric(

            "ATS Score",

            "82%",

            "+4%"

        )

    with col2:

        st.metric(

            "Career Health",

            "89%",

            "+3%"

        )

    with col3:

        st.metric(

            "Projects",

            "5",

            "+1"

        )

    with col4:

        st.metric(

            "Interview Ready",

            "74%",

            "+8%"

        )