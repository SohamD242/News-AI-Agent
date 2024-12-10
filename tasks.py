from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

## Research Task
research_task= Task(
    description=(
        "Identify the current news around {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential"
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
)

## Writing Task
write_task= Task(
    description=(
        "Compose a insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging and positive."
    ),
    expected_output='A 4 paragraph article on the topic {topic} advancements formatted as mardown',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='my-news-post.md'
)

