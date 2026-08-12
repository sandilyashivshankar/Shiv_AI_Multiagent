
import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

# Check API keys
if not os.getenv("MISTRAL_API_KEY"):
    st.error("MISTRAL_API_KEY is missing. Please add it to your .env file.")
    st.stop()

if not os.getenv("TAVILY_API_KEY"):
    st.error("TAVILY_API_KEY is missing. Please add it to your .env file.")
    st.stop()

from pipeline import run_research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Shiv Research AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "topic" not in st.session_state:
    st.session_state.topic = ""


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🧠 Shiv Research AI")

    st.caption("Multi-Agent Research Intelligence")

    st.divider()

    st.subheader("Workspace")

    if st.button(
        "🔬 New Research",
        use_container_width=True
    ):
        st.session_state.result = None
        st.session_state.topic = ""
        st.rerun()

    if st.button(
        "🗑️ Clear History",
        use_container_width=True
    ):
        st.session_state.history = []
        st.rerun()

    st.divider()

    st.subheader("🤖 AI Research Team")

    st.success("🔎 Search Agent")
    st.info("📖 Reader Agent")
    st.warning("✍️ Writer Agent")
    st.error("🧐 Critic Agent")

    st.divider()

    st.subheader("⚙️ Technology")

    st.write("• Mistral AI")
    st.write("• Tavily Search")
    st.write("• LangChain")
    st.write("• Streamlit")

    st.divider()

    st.caption("🟢 System Online")


# ============================================================
# HERO SECTION
# ============================================================

st.title("🧠 Shiv Research AI")

st.subheader(
    "Your intelligent multi-agent research assistant"
)

st.write(
    "Research any topic using a team of AI agents that "
    "search the web, analyze sources, write a structured "
    "report and review the final result."
)


# ============================================================
# DASHBOARD
# ============================================================

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "AI Agents",
        "04",
        "Search • Read • Write • Critic"
    )

with col2:
    st.metric(
        "AI Model",
        "Mistral",
        "Powered by Mistral AI"
    )

with col3:
    st.metric(
        "Web Search",
        "Tavily",
        "Real-time research"
    )

with col4:
    st.metric(
        "System",
        "Online",
        "Ready"
    )


# ============================================================
# RESEARCH AREA
# ============================================================

st.divider()

st.header("🔬 Start Deep Research")

st.write(
    "Enter a topic, question, technology, company or "
    "research problem."
)

topic = st.text_area(
    "Research Topic",
    placeholder=(
        "Example: What is the impact of Generative AI "
        "on Data Analyst careers in 2026?"
    ),
    height=120
)

start_research = st.button(
    "🚀 Start Deep Research",
    type="primary",
    use_container_width=True
)


# ============================================================
# AGENT WORKFLOW
# ============================================================

st.divider()

st.header("🤖 How Your AI Team Works")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.subheader("🔎 Search")

    st.write(
        "Finds recent and reliable information "
        "from the web using Tavily."
    )

with col2:

    st.subheader("📖 Reader")

    st.write(
        "Reads the most relevant sources and "
        "extracts deeper information."
    )

with col3:

    st.subheader("✍️ Writer")

    st.write(
        "Uses Mistral AI to create a structured "
        "and professional research report."
    )

with col4:

    st.subheader("🧐 Critic")

    st.write(
        "Reviews the report and identifies "
        "quality and accuracy issues."
    )


# ============================================================
# RESEARCH EXECUTION
# ============================================================

if start_research:

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a research topic first."
        )

    else:

        st.divider()

        st.header("⚡ Research in Progress")

        try:

            with st.status(
                "🧠 AI research team is working...",
                expanded=True
            ):

                st.write(
                    "🔎 Search Agent is searching the web..."
                )

                result = run_research_pipeline(
                    topic.strip()
                )

                st.write(
                    "📖 Reader Agent is analyzing sources..."
                )

                st.write(
                    "✍️ Writer Agent is preparing the report..."
                )

                st.write(
                    "🧐 Critic Agent is reviewing the report..."
                )

            st.session_state.result = result
            st.session_state.topic = topic.strip()

            st.session_state.history.append(
                {
                    "topic": topic.strip(),
                    "time": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    )
                }
            )

            st.success(
                "✅ Research completed successfully!"
            )

        except Exception as e:

            error_message = str(e)

            st.error(
                "❌ Research pipeline failed."
            )

            st.info(
                "Please check your API keys, dependencies "
                "and agent configuration."
            )

            with st.expander(
                "🔧 Technical Error Details"
            ):
                st.write(error_message)


# ============================================================
# RESULTS
# ============================================================

result = st.session_state.result

if result:

    st.divider()

    st.header("📑 Research Results")

    st.caption(
        f"Research Topic: {st.session_state.topic}"
    )

    report_tab, source_tab, critic_tab = st.tabs(
        [
            "📑 Final Report",
            "🔎 Sources",
            "🧐 Critic Review"
        ]
    )

    # ========================================================
    # FINAL REPORT
    # ========================================================

    with report_tab:

        report = None

        if isinstance(result, dict):

            report = (
                result.get("final_report")
                or result.get("report")
                or result.get("output")
            )

        elif isinstance(result, str):

            report = result

        if report:

            st.markdown(report)

            st.divider()

            st.download_button(
                "⬇️ Download Research Report",
                data=str(report),
                file_name="shiv_research_report.md",
                mime="text/markdown",
                use_container_width=True
            )

        else:

            st.warning(
                "No final report was generated."
            )


    # ========================================================
    # SOURCES
    # ========================================================

    with source_tab:

        if isinstance(result, dict):

            search_results = result.get(
                "search_results"
            )

            scraped_content = result.get(
                "scraped_content"
            )

            if search_results:

                st.subheader(
                    "🔎 Web Search Results"
                )

                st.markdown(
                    search_results
                )

            if scraped_content:

                st.subheader(
                    "📖 Source Analysis"
                )

                with st.expander(
                    "View detailed scraped content"
                ):

                    st.write(
                        scraped_content
                    )

        else:

            st.info(
                "Source information is not available."
            )


    # ========================================================
    # CRITIC REVIEW
    # ========================================================

    with critic_tab:

        if isinstance(result, dict):

            feedback = result.get(
                "feedback"
            )

            if feedback:

                st.subheader(
                    "🧐 AI Critic Review"
                )

                st.markdown(
                    feedback
                )

            else:

                st.info(
                    "No critic feedback was returned."
                )

        else:

            st.info(
                "Critic information is not available."
            )


# ============================================================
# RESEARCH HISTORY
# ============================================================

if st.session_state.history:

    st.divider()

    st.header("📚 Recent Research")

    for item in reversed(
        st.session_state.history[-5:]
    ):

        st.write(
            f"🔬 **{item['topic']}**"
        )

        st.caption(
            item["time"]
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🧠 Shiv Research AI • Mistral AI • Tavily • LangChain • Streamlit"
)