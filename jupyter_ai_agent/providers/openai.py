# Copyright (c) 2023-2024 Datalayer, Inc.
#
# BSD 3-Clause License

from langchain_openai import ChatOpenAI
from langchain.agents import tool
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser


def create_open_ai_agent(model: str, system_prompt: str, tools: list) -> dict:
    """Create an agent from a set of tools and an OpenAI API key."""

    # Initialize the OpenAIChat model with the API key
    llm = ChatOpenAI(
        model=model,
    )

    # Bind tools to the language model
    llm_with_tools = llm.bind_tools(tools)

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    # Create the agent pipeline
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )

    return agent
