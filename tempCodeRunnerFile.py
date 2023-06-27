from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.chains import LLMChain
from langchain.llms import OpenAI
key = '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'
llm = OpenAI(temperature=0, openai_api_key=key)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose = True)
prompt = "In what year was Ho Chi Minh born? What is this year raised to the power of 0.2?"
agent.run(prompt)