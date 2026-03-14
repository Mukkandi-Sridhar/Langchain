from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5, max_tokens=500)


class person(BaseModel):
    name : str = Field(description="name of the person")
    age : int = Field(description="age of the person")
    city : str = Field(description="city of the person")
    

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(template="tell me the name , age and place of person from {place} return the response in the format of {response_format}",input_variables=["place"],
partial_variables={"response_format": parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({"place": "hyderabad"})

print(result)
