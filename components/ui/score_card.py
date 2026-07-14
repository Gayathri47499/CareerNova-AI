import streamlit as st


def score_card(title, score, color="green"):

    if color == "green":
        emoji = "🟢"

    elif color == "yellow":
        emoji = "🟡"

    else:
        emoji = "🔴"

    st.metric(

        label=f"{emoji} {title}",

        value=f"{score}"

    )