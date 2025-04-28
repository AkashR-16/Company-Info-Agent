import asyncio
from duckduckgo_search import DDGS
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from typing import List
from pydantic import BaseModel
import pandas as pd
import yfinance as yf
from tqdm.asyncio import tqdm_asyncio  # NEW: For progress bar (optional but nice)

# -------------------------------------------
# Model Setup
# -------------------------------------------
model = OpenAIChatCompletionsModel(
    model="cogito:3b",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="secret",
    )
)

# -------------------------------------------
# Company Info Schema
# -------------------------------------------
class CompanyInfo(BaseModel):
    company_name: str
    ticker: str
    sector: str
    founding_year: int
    number_of_employees: int
    ceo_tenure_years: float
    ceo_count_since_2010: int
    average_glassdoor_rating: float
    institutional_ownership_pct: float
    board_member_count: int
    job_positions_open: int

# -------------------------------------------
# News Articles Tool
# -------------------------------------------
@function_tool
def get_news_articles(topic: str) -> str:
    print(f"Running DuckDuckGo news search for {topic}...")
    ddg_api = DDGS()
    results = ddg_api.text(f"{topic}", max_results=5)
    if results:
        news_results = "\n\n".join([
            f"Title: {result['title']}\nURL: {result['href']}\nDescription: {result['body']}"
            for result in results
        ])
        return news_results
    else:
        return f"Could not find news results for {topic}."

# -------------------------------------------
# Company Info Agent
# -------------------------------------------
agent = Agent(
    name="CompanyInfoAgent",
    instructions="""
For a given U.S.-listed company ticker, use the DuckDuckGo search tool to find:
- Full company name
- Ticker symbol
- Sector/industry
- Year the company was founded
- Current total number of employees
- Current CEO's tenure in years
- Number of different CEOs the company has had since January 1, 2010
- Average employee rating on Glassdoor
- Percentage of shares held by institutional investors
- Total number of board members
- Current Number of Job Positions Opened (globally)

Then return exactly the JSON matching the CompanyInfo schema.
Get accurate information from the web. Do deep research for each and every attribute.
""",
    tools=[get_news_articles],
    output_type=CompanyInfo,
    model=model,
)

# -------------------------------------------
# Fetch Top 500 Tickers Dynamically
# -------------------------------------------
def get_sp500_tickers() -> List[str]:
    print("Fetching latest S&P 500 tickers...")
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = table[0]
    tickers = df['Symbol'].tolist()
    print(f"Found {len(tickers)} tickers.")
    return tickers

# -------------------------------------------
# Async Worker for Single Ticker
# -------------------------------------------
async def process_ticker(ticker: str):
    try:
        info = await Runner.run(agent, ticker)
        print(f"✅ Success for {ticker}")
        return info.final_output.model_dump()
    except Exception as e:
        print(f"❌ Failed for {ticker}: {e}")
        return None

# -------------------------------------------
# Main Async Runner
# -------------------------------------------
async def main():
    all_company_data = []

    tickers = get_sp500_tickers()  # Get tickers dynamically
    # Limit for testing if needed
    # tickers = tickers[:50]  # Uncomment if you want to test only with first 50

    # Create list of coroutines
    tasks = [process_ticker(ticker) for ticker in tickers]

    # Run tasks with progress bar (optional)
    results = await tqdm_asyncio.gather(*tasks)

    # Filter out None results
    results = [res for res in results if res is not None]

    # Save to dataframe
    df = pd.DataFrame(results)
    df.to_csv("company_info_dataset.csv", index=False)
    print(f"\n✅ Saved {len(df)} companies to company_info_dataset.csv")

# -------------------------------------------
# Execute
# -------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
