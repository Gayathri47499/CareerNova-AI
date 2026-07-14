import streamlit as st
import time


def run_pipeline():

    steps = [

        "📄 Loading Resume",

        "🧠 Detecting Intent",

        "🤖 Selecting AI Agent",

        "📊 Running Analysis",

        "✨ Generating Report"

    ]

    status = st.empty()

    progress = st.progress(0)

    for i, step in enumerate(steps):

        status.info(step)

        progress.progress((i + 1) / len(steps))

        time.sleep(0.4)

    status.success("✅ CareerNova AI Report Ready")