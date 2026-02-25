from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
prompt = ChatPromptTemplate([
    ("system","you are a character of {character_name}from mahabharata"),
    ("human","explain the story of {topic} in 10 words"),
])

user = prompt.invoke({
    "character_name": "bhishma",
    "topic": "the battle of kurukshetra"
})

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5
)
rez = model.invoke(user)
print(rez.content)