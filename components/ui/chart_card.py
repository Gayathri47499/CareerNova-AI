import streamlit as st
import plotly.graph_objects as go


def ats_trend_chart(history):

    if not history:

        st.info("No ATS history available.")
        return

    scores = [item["score"] for item in history]

    labels = [f"Run {i+1}" for i in range(len(scores))]

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=labels,

            y=scores,

            mode="lines+markers",

            line=dict(
                color="#3B82F6",
                width=4
            ),

            marker=dict(
                size=10
            )

        )

    )

    fig.update_layout(

        title="ATS Progress",

        template="plotly_dark",

        height=420,

        xaxis_title="Analysis",

        yaxis_title="ATS Score"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )