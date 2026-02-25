from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

history = [
    system_message := "You are a helpful assistant",
]
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

while True:
    user_input = input("enter your question:")
    human_message = user_input
    history.append(human_message)
    res = model.invoke(history)
    print(res.content)
    if user_input.lower() == "exit":
        break
    if user_input.lower() == "history":
        print(history)
        

    
    

    