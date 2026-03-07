from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated, Optional



class Review(TypedDict):
    keythemes: Annotated[str,"Key themes in the message"]
    keycharcteristics: Annotated[str,"Key characteristics in the message"]
    sentiment: Annotated[str,"Sentiment of the message"]
    pros:Annotated[Optional[list[str]],"Pros in the message"]


model = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=500)
model_new = model.with_structured_output(Review)
message = "The most famous actors who played Lord Krishna in Mahabharat are Nitish Bharadwaj in the iconic 1988 B.R. Chopra series and Saurabh Raaj Jain in the popular 2013 Star Plus adaptation, with both portrayals widely beloved by audiences. Other actors, such as S.D. Banerjee, also played Krishna in different versions, including Ramanand Sagar's Shree Krishna.  "

res = model_new.invoke(message)

print(res)