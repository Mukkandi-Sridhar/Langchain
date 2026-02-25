from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
prompt = ChatPromptTemplate([
    ("system","you are a character of from mahabharata"),
    MessagesPlaceholder(variable_name="chathistory"),
    ("human","explain the story of {topic} in 10 words"),
])

chathistory = []
with open("chatbot/chatbothist.txt") as file:
    chathistory.extend(file.readlines())
    
res = prompt.invoke(
    {
    "topic": "the battle of kurukshetra",
    "chathistory": chathistory
    }
)


print(res)