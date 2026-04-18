import streamlit as st
import sys
import os

# Fix import path (same as your pipeline)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pipeline.pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Multi-Agent Research System")
st.markdown("Powered by Search Agent + Reader Agent + Writer + Critic")

# Input
topic = st.text_input("Enter a research topic:")

# Button
if st.button("Run Research"):
    if not topic:
        st.warning("Please enter a topic")
    else:
        with st.spinner("Running multi-agent pipeline..."):
            result = run_research_pipeline(topic)

        st.success("Research Completed!")

        # Tabs for better UI
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔎 Search Results",
            "📄 Scraped Content",
            "📝 Final Report",
            "🧠 Critic Feedback"
        ])

        with tab1:
            st.subheader("Search Results")
            st.write(result.get("search_result", ""))

        with tab2:
            st.subheader("Scraped Content")
            st.write(result.get("scraped_content", ""))

        with tab3:
            st.subheader("Final Report")
            st.write(result.get("report", ""))

        with tab4:
            st.subheader("Critic Feedback")
            st.write(result.get("feedback", ""))