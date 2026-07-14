import streamlit as st


class SessionMemory:

    """
    Stores AI conversation
    and user context.
    """

    def __init__(self):

        if "ai_memory" not in st.session_state:

            st.session_state.ai_memory = []

    def add(

        self,

        role,

        message

    ):

        st.session_state.ai_memory.append(

            {

                "role": role,

                "message": message

            }

        )

    def history(self):

        return st.session_state.ai_memory

    def clear(self):

        st.session_state.ai_memory = []