from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Review(BaseModel):
    sentiment: str = Field(description="Sentiment of the message")
    summary: str = Field(description="Short summary")

model = ChatOpenAI(
    model="gpt-4o-mini"
)

message = "i am feeling low"

new = model.with_structured_output(Review)

res = new.invoke(message)

print(res)