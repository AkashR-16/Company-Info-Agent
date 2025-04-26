# Company Info Agent 

This project builds an intelligent **Company Info Agent** that fetches detailed company information for U.S.-listed companies using a combination of:
- **DuckDuckGo Search** (for live web data)
- **OpenAI-compatible local LLM** (running on Ollama or similar)
- **Agents Framework** from `openai-agents-python`

---

## 🔖 Features
- Search and retrieve:
  - Full company name
  - Ticker symbol
  - Sector / Industry
  - Founding year
  - Number of employees
  - CEO tenure (in years)
  - CEO count since 2010
  - Average Glassdoor employee rating
  - Institutional ownership %
  - Number of board members
  - Number of open job positions (globally)
- Structured output in JSON based on a `CompanyInfo` Pydantic schema.
- Asynchronous execution for handling multiple tickers efficiently.
- Output data is stored neatly in a Pandas DataFrame for further analysis or export.

---

## 👨‍💻 Tech Stack
- Python 3.10+
- [openai-agents-python](https://pypi.org/project/openai-agents-python/)
- [duckduckgo-search](https://pypi.org/project/duckduckgo-search/)
- [Ollama](https://ollama.ai/) or any OpenAI-compatible local LLM endpoint
- Pydantic
- Pandas

---

## 🔹 Installation

1. Clone the repository:
```bash
https://github.com/yourusername/company-info-agent.git
cd company-info-agent
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Start your local LLM server (Ollama or custom OpenAI-compatible endpoint).
Example:
```bash
ollama run cogito:3b
```

4. Run the script:
```bash
python main.py
```

---

## 👀 Example Output

```
CompanyInfo(
    company_name='Apple Inc.',
    ticker='AAPL',
    sector='Technology',
    founding_year=1976,
    number_of_employees=161000,
    ceo_tenure_years=13.5,
    ceo_count_since_2010=1,
    average_glassdoor_rating=4.2,
    institutional_ownership_pct=60.5,
    board_member_count=8,
    job_positions_open=4200
)
```

---

## 📘 Project Structure

```
company-info-agent/
|├── main.py         # Main agent script
|├── requirements.txt # Python dependencies
|└── README.md       # This file
```

---

## 🔍 Notes
- **Accuracy:** DuckDuckGo searches are not guaranteed to always return the most up-to-date results. Manual verification may still be required.
- **Expandability:** You can easily add more fields or integrate more powerful retrieval tools like web scrapers or APIs.

---

## 💜 Contributions
Pull requests, improvements, and suggestions are welcome!

---

## 📅 License
[MIT License](LICENSE)

---

## 🛍️ Future Enhancements
- Integrate real financial APIs (e.g., Yahoo Finance, Alpha Vantage)


