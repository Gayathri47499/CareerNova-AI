import streamlit as st

from chat.chat_service import ChatService
from memory.session_memory import SessionMemory

from components.ui.chat_history import show_chat_history



def show():

    st.title("🤖 CareerNova AI Assistant")

    st.write(

        "Ask anything about your career."

    )

    question = st.text_input(

        "Your Question"

    )

    if st.button(

        "Send",

        use_container_width=True

    ):

        profile = st.session_state.get(

            "resume_profile"

        )

        service = ChatService()

        with st.spinner(

            "Thinking..."

        ):

            response = service.ask(

                profile,

                question

            )

        st.divider()

        st.markdown(response)
        memory = SessionMemory()

        show_chat_history(

        memory.history()

)