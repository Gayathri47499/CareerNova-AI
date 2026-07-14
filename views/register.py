import streamlit as st

from auth.auth_service import AuthService


def show():

    st.title("📝 Register")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(

        "Password",

        type="password"

    )

    if st.button(

        "Create Account",

        use_container_width=True

    ):

        service = AuthService()

        service.register(

            name,

            email,

            password

        )

        st.success(

            "Account Created"

        )
        st.divider()

if st.button("Already have an account? Login"):

    st.session_state.current_page = "login"

    st.rerun()