# 🤖 Shiv AI Multi-Agent Research System

> **A production-style multi-agent research application built with LangChain, Mistral AI, Tavily, web scraping, and Streamlit.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://shivaimultiagent.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/sandilyashivshankar/Shiv_AI_Multiagent)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-1C3C3C)](https://www.langchain.com/)
[![Mistral AI](https://img.shields.io/badge/Mistral%20AI-LLM-FF7000)](https://mistral.ai/)
[![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-111827)](https://tavily.com/)

## 🌐 Live Application

### [🚀 Open Shiv AI Multi-Agent](https://shivaimultiagent.streamlit.app/)

Run a research topic through the deployed Streamlit application and get a structured research report with source-aware findings and critic feedback.

---

## 📌 Overview

**Shiv AI Multi-Agent** is an AI-powered research workflow designed to break complex research tasks into specialized stages instead of relying on a single LLM call.

The system coordinates multiple agents and chains to:

1. 🔎 **Search** the web for recent and relevant information.
2. 📖 **Read** selected sources by scraping deeper page content.
3. ✍️ **Write** a structured research report from the gathered evidence.
4. 🧠 **Critique** the final report and provide a quality score with improvement areas.

The application uses **Mistral AI** as the language model, **Tavily** for web search, **BeautifulSoup + Requests** for source extraction, and **Streamlit** for the user interface.

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │   User Research     │
                         │       Topic         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Search Agent      │
                         │  Tavily Web Search  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Reader Agent     │
                         │ URL Scraping / Read │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Writer Chain     │
                         │ Structured Report   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Critic Chain     │
                         │ Score + Improvements│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Final Research    │
                         │ Report + Feedback   │
                         └─────────────────────┘
```

### Pipeline

**Topic → Search Agent → Reader Agent → Writer → Critic → Final Output**

The workflow implemented in `pipeline.py` follows these four stages directly. fileciteturn8file0

---

## ✨ Key Features

- **Multi-agent research workflow** with specialized roles.
- **Mistral Small** powered reasoning and report generation.
- **Tavily web search** for current research sources.
- **URL scraping** for deeper source analysis.
- **Structured reports** containing Introduction, Key Findings, Conclusion, and Sources.
- **Research critic** that scores the generated report and identifies strengths and improvement areas.
- **Streamlit interface** for an accessible web-based experience.
- **Environment-based API key configuration** using `.env` variables.
- **Clear separation of concerns** across agents, tools, pipeline, and UI.

---

## 🧩 Project Structure

```text
Shiv_AI_Multiagent/
│
├── Multi Agent System/
│   ├── agents.py       # Search agent, Reader agent, Writer and Critic chains
│   ├── pipeline.py     # End-to-end multi-agent research workflow
│   ├── tools.py        # Tavily search and URL scraping tools
│   └── app.py          # Streamlit application
│
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

The repository currently keeps the application code inside the `Multi Agent System` directory. fileciteturn6file0

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application development |
| **LangChain** | Agent and LLM orchestration |
| **Mistral AI** | Large language model |
| **Tavily** | Web search and research discovery |
| **BeautifulSoup** | HTML parsing and content extraction |
| **Requests** | HTTP requests for source scraping |
| **Streamlit** | Web application interface |
| **python-dotenv** | Environment variable management |

The current dependency set includes LangChain, Mistral integration, Tavily, BeautifulSoup, Requests, Streamlit, and supporting libraries. fileciteturn4file0

---

## ⚙️ How It Works

### 1. Search Agent
The Search Agent uses Tavily to find up to five relevant web results for a research topic and returns titles, URLs, and snippets. fileciteturn7file0 fileciteturn9file0

### 2. Reader Agent
The Reader Agent uses a scraping tool to retrieve page content, remove common non-content HTML elements, and extract readable text for deeper analysis. fileciteturn7file0 fileciteturn9file0

### 3. Writer Chain
The Writer creates a structured research report from the search results and scraped content. The current report format includes:

- Introduction
- Key Findings
- Conclusion
- Sources

The prompt also instructs the writer to avoid invented sources and statistics. fileciteturn7file0

### 4. Critic Chain
The Critic evaluates the generated report using a score out of 10, lists strengths, highlights areas to improve, and provides a one-line verdict. fileciteturn7file0

---

## 🔐 Environment Variables

Create a `.env` file and add your API credentials:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The application reads these values from environment variables and raises an error when the required keys are missing. fileciteturn7file0 fileciteturn9file0

> **Security:** Never commit your `.env` file or API keys to GitHub.

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sandilyashivshankar/Shiv_AI_Multiagent.git
cd Shiv_AI_Multiagent
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` in the project directory and add your Mistral and Tavily API keys.

### 5. Start the Streamlit application

```bash
streamlit run "Multi Agent System/app.py"
```

Then open the local Streamlit URL shown in your terminal.

---

## 📊 Example Workflow

```text
Research Topic
      │
      ▼
Web Discovery
      │
      ▼
Source Selection & Scraping
      │
      ▼
Evidence Gathering
      │
      ▼
AI Research Report
      │
      ▼
Quality Review
      │
      ▼
Final Report + Critic Feedback
```

---

## 🎯 Why This Project Matters

Traditional LLM applications often depend on a single prompt-response cycle. This project demonstrates a more structured approach where different responsibilities are assigned to specialized components.

This design makes the workflow easier to understand, extend, and debug while demonstrating practical concepts in:

- Agentic AI
- LLM orchestration
- Tool calling
- Web research automation
- Information extraction
- Prompt engineering
- AI-generated report evaluation
- Streamlit application development

---

## 🔮 Future Improvements

Potential extensions for the project include:

- Parallel source research with multiple researcher agents.
- Source ranking and credibility scoring.
- Citation-aware report generation.
- Automatic retry and fallback strategies for failed sources.
- Persistent research history and report storage.
- Export reports to PDF or Markdown.
- Human-in-the-loop approval before final report generation.
- More advanced multi-agent collaboration and memory.

---

## 📎 Project Links

**Live Application:** https://shivaimultiagent.streamlit.app/

**GitHub Repository:** https://github.com/sandilyashivshankar/Shiv_AI_Multiagent

---

## 👨‍💻 Author

### Shiv Shankar Tiwari

Data Analyst | AI & ML | Prompt Engineering | Agentic AI

Built with a focus on practical AI automation, research workflows, and intelligent data-driven applications.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub and sharing feedback or ideas for improvement.

---

<p align="center">
  <strong>Built with Python • LangChain • Mistral AI • Tavily • Streamlit</strong>
</p>
