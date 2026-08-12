import os

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not MISTRAL_API_KEY:
    raise ValueError(
        "MISTRAL_API_KEY is missing. "
        "Please add it to your .env file."
    )


# ============================================================
# MISTRAL MODEL
# ============================================================

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
    api_key=MISTRAL_API_KEY,
)


# ============================================================
# 1. SEARCH AGENT
# ============================================================

def build_search_agent():

    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt=(
            "You are an expert web research agent. "
            "Search for reliable and relevant information "
            "about the user's research topic. "
            "Use the available web search tool and return "
            "useful findings with source URLs."
        ),
    )


# ============================================================
# 2. READER AGENT
# ============================================================

def build_reader_agent():

    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt=(
            "You are an expert research reader. "
            "Analyze the provided web sources carefully. "
            "Extract important facts, evidence, statistics, "
            "and useful information. "
            "Be factual and avoid unsupported claims."
        ),
    )


# ============================================================
# 3. WRITER CHAIN
# ============================================================

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert research writer.

Your job is to create clear, structured, factual,
and insightful research reports.

Use only the information available in the
research gathered by the research agents.
"""
        ),

        (
            "human",
            """
Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure the report as:

# Introduction

Provide a clear introduction to the topic.

# Key Findings

Provide a minimum of 3 well-explained findings.

# Conclusion

Summarize the most important insights.

# Sources

List all URLs found in the research.

Requirements:

- Be detailed.
- Be factual.
- Be professional.
- Do not invent sources.
- Do not invent statistics.
- Clearly distinguish facts from interpretations.
"""
        ),
    ]
)


writer_chain = (
    writer_prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# 4. CRITIC CHAIN
# ============================================================

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a sharp and constructive research critic.

Evaluate research reports carefully.
Be honest, specific, and objective.
"""
        ),

        (
            "human",
            """
Review the research report below and evaluate it strictly.

Report:

{report}

Respond in exactly this format:

Score: X/10

Strengths:

- ...
- ...
- ...

Areas to Improve:

- ...
- ...
- ...

One line verdict:

...
"""
        ),
    ]
)


critic_chain = (
    critic_prompt
    | llm
    | StrOutputParser()
)