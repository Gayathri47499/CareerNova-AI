import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🚀 CareerNova AI")

        user = st.session_state.get("user")

        if user:

            st.success("🟢 Online")

            st.markdown("### 👋 Welcome")

            st.markdown(f"**{user[1]}**")

        st.divider()

        page = st.radio(

            "Navigation",

            [

                "Dashboard",

                "Resume",

                "ATS",

                "Career",

                "Interview",

                "Analytics",

                "Chat",

                "Settings"

            ]

        )

        st.divider()

        st.caption("CareerNova AI v1.0")

        st.caption("Built with ❤️ using")

        st.caption("Python • Streamlit • LangGraph • Groq")

        st.divider()

        if st.button(

            "🚪 Logout",

            use_container_width=True

        ):

            st.session_state.clear()

            st.session_state.logged_in = False

            st.session_state.current_page = "login"

            st.rerun()

    return page