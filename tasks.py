from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool, web_search_tool 

research_task = Task(
    description=(
        """
        Research and extract key insights on {topic} by analyzing YouTube videos from the specified channel 
        and validating the information using web searches. Identify key trends, expert opinions, 
        and factual data to enhance the blog content.
        """
    ),
    expected_output="A structured research summary combining YouTube insights and verified web data.",
    tools=[yt_tool, web_search_tool],
    agent=blog_researcher,
)

write_task = Task(
    description=(
        """
        Using the structured research summary, craft a compelling and well-verified blog post on {topic}. 
        The article should integrate insights from YouTube videos and cross-checked web sources to ensure 
        accuracy, credibility, and depth. The tone should be engaging, structured, and suitable for both 
        technical and general audiences.
        """
    ),
    expected_output="A well-researched and engaging blog post on {topic}, stored in 'new-blog-post.md'.",
    tools=[],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)

