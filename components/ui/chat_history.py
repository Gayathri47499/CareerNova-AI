import streamlit as st


def show_chat_history(history):

    if not history:

        return

    st.divider()

    st.subheader("💬 Conversation")

    for item in history:

        if item["role"] == "user":

            st.chat_message(

                "user"

            ).write(

                item["message"]

            )

        else:

            st.chat_message(

                "assistant"

            ).write(

                item["message"]

            )