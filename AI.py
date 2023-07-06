from langchain import PromptTemplate
from langchain.llms import OpenAI

key = 'key'
llm = OpenAI(temperature=0, openai_api_key=key)
template = """/
You are a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate.from_template(template)
s = prompt.format(product="colorful socks")
llm(s)