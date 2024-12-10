from crewai import Agent
from tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import LLM

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)
 

## Creating a senior researcher

news_researcher= Agent(
    role="Senior Blog Reasearcher",
    goal="Uncover ground breaking Technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
## Creating a senior writer agent responsible in writing news blog

news_writer= Agent(
    role="Senior News Writer",
    goal="Narrate compelling blogs about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        '''Expert in simplifying complex topics, you craft engaging narrations that captivate and educate, bringing new discoveries to light in an accessible manner.'''
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

