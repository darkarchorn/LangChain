from langchain.llms import OpenAI
from langchain.chains import ConversationChain
key = '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'
llm = OpenAI(temperature=0, openai_api_key=key)
conversation = ConversationChain(llm=llm, verbose = True)
conversation.predict(input = "Can we talk about something interesting?")