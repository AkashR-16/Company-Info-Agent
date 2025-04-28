# Company Info Agent 📈

This project scrapes detailed company information from S&P 500 tickers using autonomous agents powered by a local LLM.
It builds a rich dataset including company name, sector, founding year, CEO tenure, Glassdoor ratings, and more.

---

## 📊 Features
- Dynamically fetches **live S&P 500 tickers** from Wikipedia and processes all companies in parallel.
- Integrates **DuckDuckGo search** for fresh news articles.
- Uses **local LLM** inference via Ollama (`cogito:3b`) for intelligent extraction.
- **Progress bar** to monitor scraping live.
- Builds a **structured CSV dataset** automatically.
- Error handling: One ticker's failure won't crash the full pipeline.

---

## 📜 Scripts Overview
- **`basic.py`**: A basic program created for a predefined list of tickers (`AAPL`, `MSFT`, `GOOGL`, `AMZN`, `TSLA`).
- **`main.py`**: The main agentic system that dynamically fetches the current S&P 500 tickers and processes them.

---

## 📂 Output Example
The final dataset (`company_info_dataset.csv`) contains:

| Company Name | Ticker | Sector | Founding Year | Employees | CEO Tenure (years) | ... |
|--------------|--------|--------|---------------|-----------|--------------------|-----|
| Apple Inc.   | AAPL   | Tech   | 1976          | 164,000   | 3.5                | ... |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/AkashR-16/Company-Info-Agent.git
cd Company-Info-Agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> Requirements include: `pandas`, `duckduckgo-search`, `yfinance`, `openai-agents-python`, `pydantic`, `tqdm`

### 3. Set up your Ollama server
Make sure your LLM (like `cogito:3b`) is running locally via Ollama at `http://localhost:11434/v1`.

### 4. Run the script
#### For basic ticker list (5 companies):
```bash
python basic.py
```

#### For dynamic S&P 500 ticker scraping:
```bash
python main.py
```

The scraping will begin! Check `company_info_dataset.csv` once done.

---

## 🔧 Project Structure
```
.
├── main.py          # Main agentic system for full S&P 500 scraping
├── basic.py         # Basic program for a few predefined tickers
├── requirements.txt # Python package requirements
├── README.md        # This file
└── company_info_dataset.csv # Output dataset (after run)
```

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas** — Data manipulation and CSV generation
- **DuckDuckGo Search API** — Web search for company news
- **Yahoo Finance (`yfinance`)** — Ticker and financial data
- **OpenAI Agents Python SDK** — Agentic architecture
- **Ollama** — Local LLM server (running `cogito:3b` model)
- **Pydantic** — Data validation and typing
- **TQDM** — Progress bars

---

## 🔐 License
MIT License.

Feel free to use, modify, and contribute!



---
