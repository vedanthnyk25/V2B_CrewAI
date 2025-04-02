from crewai_tools import YoutubeChannelSearchTool, SerpAPISearchTool
from dotenv import load_dotenv
import os

load_dotenv()

serp_api_key= os.getenv("SERP_API_KEY")

#Initialise the tool with a specific YT handle to target your search
channel="sentdex"
yt_tool= YoutubeChannelSearchTool(youtube_channel_handle={channel})
web_search_tool = SerpAPISearchTool(api_key=serp_api_key) 
