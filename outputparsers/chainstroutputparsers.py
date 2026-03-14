from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5, max_tokens=500)

prompt1 = ChatPromptTemplate.from_messages(["tell about this in 2 lines {topic}"])


prompt2 = ChatPromptTemplate.from_messages(["make the 2 line sentense into 1 line sentense {topic2}"])

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "shakuni"})

print(result)