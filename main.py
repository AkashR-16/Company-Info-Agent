import asyncio
from duckduckgo_search import DDGS
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from typing import List
from pydantic import BaseModel
import pandas as pd


model=OpenAIChatCompletionsModel(
    model="cogito:3b",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="secret",
    )
)

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
Get accurate information from the web. do deep research for each and every attribute.
""",
    tools=[get_news_articles],
    output_type=CompanyInfo,
    model=model,
)

# 3) Loop over a list of tickers
tickers = [
    "AAPL", 
    "MSFT",
    "GOOGL",
    "AMZN", 
    "TSLA" 
]

async def main():
    all_company_data = []
    for ticker in tickers:
        info = await Runner.run(agent, ticker)
        print(info.final_output)
        all_company_data.append(info.final_output.model_dump())

    df = pd.DataFrame(all_company_data)
    print(df)

# Now actually run the async function
asyncio.run(main())