from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5, max_tokens=500)

prompt1 = ChatPromptTemplate.from_messages(["tell about this in 4 lines {topic}"])
result1 = model.invoke(prompt1.format_messages(topic="shakuni")).content
print("agent 1 result:")
print(result1)

prompt2 = ChatPromptTemplate.from_messages(["make the 4 line sentense into 1 line sentense {topic2}"])
result2 = model.invoke(prompt2.format_messages(topic2=result1))
print("agent 2 result:")
print(result2.content)
