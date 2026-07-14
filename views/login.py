import streamlit as st

from auth.auth_service import AuthService


def show():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(

        "Password",

        type="password"

    )

    if st.button(

        "Login",

        use_container_width=True

    ):

        service = AuthService()

        user = service.login(

            email,

            password

        )

        if user:

            st.session_state.logged_in = True

            st.session_state.user = user

            st.session_state.current_page = "dashboard"

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Credentials")

    st.divider()

    if st.button("Create New Account"):

        st.session_state.current_page = "register"

        st.rerun()