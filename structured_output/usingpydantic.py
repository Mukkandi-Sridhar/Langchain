from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5, max_tokens=500)

class Review(BaseModel):
    summary: str = Field(description="A concise summary of the message")
    name: str = Field(description="Name of the person in the message")
    characters: list[str] = Field(description="Key characteristics in the message")
    
new_model = model.with_structured_output(Review)

message = "The most famous actors who played Lord Krishna in Mahabharat are Nitish Bharadwaj in the iconic 1988 B.R. Chopra series and Saurabh Raaj Jain in the popular 2013 Star Plus adaptation, with both portrayals widely beloved by audiences. Other actors, such as S.D. Banerjee, also played Krishna in different versions, including Ramanand Sagar's Shree Krishna.  "

res = new_model.invoke(message)

print(res)