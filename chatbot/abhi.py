from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

message = input("Enter your message: ")

result = model.invoke(message)
print(result.content)