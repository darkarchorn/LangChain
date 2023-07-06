# Báo cáo thực tập
# LangChain 🦜🔗

## **26/06/2023**
- Đọc và tham khảo các tài liệu và video tutorial về LangChain  
Overview: [Youtube Overvew by AssemblyAI](https://www.youtube.com/watch?v=RoR4XJw8wIc&ab_channel=AssemblyAI)  
Github repository:  
[kyrolabs' Awesome Langchain](https://github.com/kyrolabs/awesome-langchain)  
[hwchase17's Langchain](https://github.com/hwchase17/langchain)  
- Các tài liệu khác:  
[Official Documentation](https://python.langchain.com/docs/get_started/introduction.html)  
[Google Colab LangChain](https://colab.research.google.com/drive/1VOwJpcZqOXag-ZXi-52ibOx6L5Pw-YJi?usp=sharing#scrollTo=nTDgRy0jKDkP)  
[Crash Course (Youtube)](https://www.youtube.com/watch?v=LbT1yp6quS8&ab_channel=PatrickLoeber)

## **Tóm tắt**: 
## Installation:  
```bat
pip install openai
pip install langchain
pip install huggingface_hub
```
LangChain là một framework hỗ trợ phát triển các ứng dụng được hỗ trợ bởi các language module, bao gồm:
1. [**Models I/O**](https://python.langchain.com/docs/modules/model_io/): Interface with language models  
- Langchain cung cấp interface standard và extendable cho nhiều loại LLM (Large Language Models). Phần lớn model hoạt động thông qua API nhưng ta cũng có thể sử dụng local model.  
- Các nhà cung cấp LLM: [Integrations](https://python.langchain.com/en/latest/modules/models/llms/integrations.html)
- Example code:
``` python
from langchain.llms import OpenAI
key = 'key'
llm = OpenAI(temperature=0, openai_api_key=key)
text = "How many days is it from 26/06/2002 to 27/09/2020"
print(llm(text))
```

- Langchain sử dụng prompt template để xử lý tối ưu hơn
- Bình thường khi ta sử dụng một ứng dụng sử dụng LLM, ta không gửi trực tiếp user input tới LLM. Thay vào đó, ta cần đưa input đó và xây dựng một template, sau đó mới gửi lại cho LLM.
- Example code:
```python
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
```
Tuy nhiên ta không thể truyền trực tiếp vào template như này 
```python
llm(s)
``` 
do ta gặp TypeError: Object of type PromptTemplate is not JSON serializable. Ta phải sử dụng đến Chain  

3. [**Chains**](https://python.langchain.com/docs/modules/chains/): Construct sequences of calls
- Tuy việc sử dụng LLM một cách riêng biệt không có ảnh hướng quá nhiều đối với các dự án đơn giản, nhưng khi đối mặt với các ứng dụng phức tạp hơn, ta cần sử dụng chaining LLMs (either with each other or with other components)
- LangChain cho ta interface ***Chain*** nhằm phục vụ các ứng dụng "chained". Ta định nghĩa một Chain một cách tổng quát như một chuỗi các call tới các component, đồng thời có thể chứa các chain khác. Nói dễ hiểu hơn thì Chain hỗ trợ các prompt có nhiều bước, ví dụ như "Do George Washington mất năm 1799, Obama sinh năm 1961, nên 2 người không thể trò chuyện với nhau được"
- Implementation:
```python
class Chain(BaseModel, ABC):
    """Base interface that all chains should implement."""

    memory: BaseMemory
    callbacks: Callbacks

    def __call__(
        self,
        inputs: Any,
        return_only_outputs: bool = False,
        callbacks: Callbacks = None,
    ) -> Dict[str, Any]:
        ...
```
- Một số chức năng của Chain:
  + Async API: hỗ trợ async qua việc sử dụng thư viện asyncio
  + Hỗ trợ các phương thức call: Các lớp kế thừa từ Chain offer một số cách sử dụng chain logic
  + Custom chain: Có thể implement custom chain
  + Debugging chains
  + Loading from LangChainHub
  + Adding memory (state)
- Example code:
```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain only specifying the input variable.
print(chain.run("colorful socks"))
```
- Trong trường hợp có nhiều biến:
```python
prompt = PromptTemplate(
    input_variables=["company", "product"],
    template="What is a good name for {company} that makes {product}?",
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run({
    'company': "ABC Startup",
    'product': "colorful socks"
    }))
```
- Ngoài ra ta có thể sử dụng *LLMChain*
```py
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is a good name for a company that makes {product}?",
            input_variables=["product"],
        )
    )
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
chat = ChatOpenAI(temperature=0.9)
chain = LLMChain(llm=chat, prompt=chat_prompt_template)
print(chain.run("colorful socks"))
```
4. [**Agents and Tools**](https://python.langchain.com/docs/modules/agents/): Let chains choose which tools to use given high-level directives
- Interface Agent cung cấp sự linh hoạt cho các ứng dụng mà cần đến các tool (tùy vào user input)
- Một số Toolkit phổ biến
  + Azure Cognitive Services Toolkit
  + CSV Agent
  + Document Comparison
  + Gmail Toolkit
  + Jira
  + JSON Agent
  + Office365 Toolkit
  + OpenAPI agents
  + Natural Language APIs
  + Pandas Dataframe Agent
  + PlayWright Browser Toolkit
  + PowerBI Dataset Agent
  + Python Agent
  + Spark Dataframe Agent
  + Spark SQL Agent
  + Vertorstore Agent

- Cách dùng Tools:
```py
from langchain.agents import load_tools
tool_names = [...]
tools = load_tools(tool_names)
```
- Một số tool cần truyền vào LLM
```py
from langchain.agents import load_tools
tool_names = [...]
llm = ...
tools = load_tools(tool_names, llm=llm)
```
- Example code:
```py
from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.chains import LLMChain
from langchain.llms import OpenAI
key = 'key'
llm = OpenAI(temperature=0, openai_api_key=key)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose = True)
prompt = "In what year was Ho Chi Minh born? What is this year raised to the power of 0.2?"
agent.run(prompt)
```
5. [**Memory**](https://python.langchain.com/docs/modules/memory/): Persist application state between runs of a chain
- Add State vào Chains và Agents  
- Example code:
```py
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
key = 'key'
llm = OpenAI(temperature=0, openai_api_key=key)
conversation = ConversationChain(llm=llm, verbose = True)
conversation.predict(input = "Can we talk about something interesting?")
```
6. [**Callbacks**](https://python.langchain.com/docs/modules/callbacks/): Log and stream intermediate steps of any chain
- Giúp thuận tiện hơn trong việc logging, monitoring, streaming...

7. Document Loader ([tham khảo](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html))
- Example code:
```py
from langchain.document_loaders import NotionDirectoryLoader

loader = NotionDirectoryLoader("Notion_DB")

docs = loader.load()
```

8. Indexes
- Đây là cách mà LLM xử lý các dữ liệu có khối lượng lớn và thao tác với chúng. Module này chứa các chức năng như sau:
  + Embedding (nhúng): là một đại diện dạng số hóa biểu diễn một khối lượng thông tin, như văn bản, tài liệu, hình ảnh, âm thanh,...
  + Text Splitters: Chia đoạn văn bản dài thành các chunk (khối) để xử lý dễ dàng hơn
  + Vectorstores: Hiểu đơn giản là ví dụ mình muốn ăn pizza, mà pizza đó phải đến từ nhà hàng 5 sao, bill rẻ lại còn vận chuyển nhanh và miễn phí, thì các criteria đó giúp việc tìm ra chỗ nhà hàng nào phù hợp, chính xác và liên quan nhất. Các điều kiện trên chính là các vector giúp LLM tìm đc chính xác thứ mình cần tìm