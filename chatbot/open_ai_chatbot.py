from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.5
)


history = [
    SystemMessage(content="You are a helpful assistant"),
]


while True:
    user_input = input("enter your question:")

    if user_input.lower() == "exit":
        break   
    if user_input.lower() == "history":
        print(history) 
        continue 
        
    human_msg = HumanMessage(content=user_input)
    history.append(human_msg.content)
    ai_msg = model.invoke(history)
    history.append(ai_msg.content)
    print(ai_msg.content)