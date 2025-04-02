from crewai import Agent
from tools import yt_tool, web_search_tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv["GROQ_API_KEY"]

llm = ChatGroq(
        model_name="llama-3.3-70b-versatile", 
        api_key= groq_api_key  
)

##Create a senior blog content researcher

blog_researcher = Agent(
    role="AI Research & Content Curator",
    goal="Extract insights from YouTube videos and cross-verify with web content for {topic}.",
    verbose=True,
    memory=True,
    backstory=''' 
        An advanced AI research agent that specializes in collecting, analyzing, and validating insights from multiple sources. 
        It extracts key information from YouTube videos and cross-verifies the details using web articles, research papers, and 
        authoritative sources. This ensures high-quality, well-researched content for blog writing.
    ''',
    tools=[yt_tool, web_search_tool],  # Now uses both YouTube & Web Search
    allow_delegation=True,
    llm=llm
)


## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role="AI-Powered Tech Blog Writer",
    goal="Craft compelling, well-structured, and engaging blog articles based on insights extracted from YouTube videos on {topic}.",
    verbose=True,
    memory=True,
    backstory= ''' 
        A highly skilled AI-driven blog writer, specializing in transforming complex technical concepts into engaging, well-structured, 
        and reader-friendly narratives. With expertise in AI, Data Science, Machine Learning, Generative AI, and cutting-edge technologies, 
        this agent crafts insightful articles that resonate with both technical and non-technical audiences. 

        It ensures that each blog post maintains clarity, storytelling flow, and thought leadership, while also optimizing content for 
        readability and impact. The agent adapts its tone based on the target audience—whether explaining AI breakthroughs to beginners or 
        providing in-depth technical insights for experts. 
    ''',
    tools=[],
    allow_delegation=False,
    llm=llm
)

