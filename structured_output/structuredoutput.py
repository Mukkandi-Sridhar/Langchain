from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict
from pydantic import BaseModel


#scheme

class Review(TypedDict):
    answer: str
    sentiment: str
    


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=50)
model_new = model.with_structured_output(Review)
message = "i met with an accident today"

res = model_new.invoke(message)

print(res)