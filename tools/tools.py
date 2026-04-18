from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# loading tavily client
tavily = TavilyClient(api_key=TAVILY_API_KEY)


# Creating tools using @tool decorator

@tool
def web_search(query:str) -> str:
    """
    Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets
    
    """

    results = tavily.search(query=query,max_results=5)
    
    out = []

    for r in results["results"]:
        out.append(
            f"Title: {r['title']} \n URL: {r['url']} \n Snippet: {r['content'][:300]}\n"

        )
    # out = [f"Title: {r['title']} \n URL: {r['url']} \n Snippet: {r['content'][:300]}\n"  for r in results["results"]]   

    return "\n---------\n".join(out)


    # return results


# print(web_search.invoke("What are the recent news about TCS nasik?"))



@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""

    try:
        resp = requests.get(url, timeout=8, headers= {"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]

    except Exception as e:
        return f"Could not scrape URL ; {str(e)}"
    


# print(scrape_url.invoke("https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/"))





