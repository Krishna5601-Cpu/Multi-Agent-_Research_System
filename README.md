# Multi-Agent Research System

A small multi-agent pipeline that researches a topic on the web and produces a structured report, then critiques it, Built with LangChain, OpenAI and Tavily.

## How it works

```
topic
  │
  ▼
Search agent ──► Reader agent ──► Writer chain ──► Critic chain
 (Tavily)        (scrapes a URL)   (drafts report)  (scores report)
```

1. **Search agent** finds recent, relevant sources for the topic using Tavily.
2. **Reader agent** picks the most relevant URL and scrapes it for deeper content.
3. **Writer chain** combines both into a report: introduction, key findings, conclusion, sources.
4. **Critic chain** reviews the report and returns a score, strengths, areas to improve and a one-line verdict.

## Project structure

```
.
├── main.py                  # entry point
├── research_system/
│   ├── __init__.py
│   ├── agents.py            # LLM setup, agents, writer and critic chains
│   ├── tools.py             # web_search (Tavily) and scrape_url tools
│   └── pipeline.py          # orchestrates the four steps
├── requirements.txt
├── .env.example             # copy to .env and add your keys
└── README.md
```

## Setup

```bash
git clone https://github.com/Krishna5601-Cpu/Multi-Agent-_Research_System.git
cd Multi-Agent-_Research_System

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env             # then edit .env with your keys
```

You need two API keys:

- `OPENAI_API_KEY` from [OpenAI](https://platform.openai.com/)
- `TAVILY_API_KEY` from [Tavily](https://tavily.com/)

## Usage

```bash
python main.py
```

Enter a topic when prompted. The script prints the output of each step (search results, scraped content, final report, critic feedback).
