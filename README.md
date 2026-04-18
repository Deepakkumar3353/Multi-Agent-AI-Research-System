# Multi-Agent AI Research System

A lightweight multi-agent research pipeline that uses specialized agents to search, scrape, write, and critique research reports. Built with LangChain, Google Generative AI (Gemini), Tavily search, and Streamlit for a simple UI.

**Key Features**
- Search Agent: Finds recent, reliable web sources using the Tavily search tool.
- Reader Agent: Scrapes selected URLs and returns cleaned text for deeper reading.
- Writer Chain: Generates a structured research report from collected material.
- Critic Chain: Reviews and scores the generated report, providing actionable feedback.
- Streamlit UI: Simple interface to run the pipeline and view results.

**Repository Structure**
- [app.py](app.py) — Minimal Streamlit app entry that calls the pipeline and shows results.
- [main.py](main.py) — Alternative, richer Streamlit UI (more styling and pipeline controls).
- [requirement.txt](requirement.txt) — Python dependencies used by the project.
- [agents/agents.py](agents/agents.py) — Agent and chain definitions (search, reader, writer, critic).
- [tools/tools.py](tools/tools.py) — Tool implementations: `web_search` (Tavily) and `scrape_url` (BeautifulSoup + requests).
- [pipeline/pipeline.py](pipeline/pipeline.py) — Orchestrates the multi-agent research pipeline.

Getting Started
---------------

1. Clone the repository and change into the project directory.

2. Create and activate a Python virtual environment (recommended):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirement.txt
```

Environment variables
---------------------
Create a `.env` file in the project root with the following keys:

```
GEMINI_API_KEY=your_google_generative_api_key
TAVILY_API_KEY=your_tavily_api_key
```

- `GEMINI_API_KEY` is used by the `langchain_google_genai` integration (`ChatGoogleGenerativeAI`).
- `TAVILY_API_KEY` is used by the `tavily` client for web search.

Usage
-----

- Run the simple app:

```bash
streamlit run app.py
```

- Or run the richer UI:

```bash
streamlit run main.py
```

Programmatic usage
-------------------
You can call the pipeline directly from Python:

```python
from pipeline.pipeline import run_research_pipeline
result = run_research_pipeline("your research topic")
```

Notes on components
-------------------
- `agents/agents.py` defines the LLM (`ChatGoogleGenerativeAI`) and constructs the agents and chains:
  - `build_search_agent()` — agent using the `web_search` tool.
  - `build_reader_agent()` — agent using the `scrape_url` tool.
  - `writer_chain` and `critic_chain` — prompt templates piped to the LLM and parsed.
- `tools/tools.py` contains two `@tool` functions used by agents:
  - `web_search(query: str) -> str` — calls Tavily and returns top results (title, URL, snippet).
  - `scrape_url(url: str) -> str` — fetches and returns cleaned text from a URL (uses requests + BeautifulSoup).
- `pipeline/pipeline.py` orchestrates the flow: run search agent → run reader agent on top result → generate report → critique report.

Troubleshooting
---------------
- If agents fail to start, ensure your `.env` variables are set and valid.
- If `tavily` or `google-generativeai` calls fail, check network access and API quotas.
- On Windows, ensure the virtual environment activation uses the `Scripts` path shown above.

Security & privacy
------------------
- Do not commit your `.env` or API keys to version control. Use a secure secret manager in production.

Extending the project
---------------------
- Add more tools (other search sources, PDF scraping, or academic APIs).
- Persist results (e.g., Redis or a lightweight DB) to cache searches and reports.
- Add authentication and a simple API layer using `FastAPI` to expose the pipeline.

License & Contribution
----------------------
This project is provided as-is. Feel free to open issues or contribute improvements via pull requests.

Contact
-------
For questions, open an issue in this repository.
