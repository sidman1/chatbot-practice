import os
from dotenv import load_dotenv
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPEN_AI_MODEL = "gpt-3.5-turbo"

PROMPT_COUNTRY_INFO= """
Provide information about {country}
{format_instructions}
"""

class Country(BaseModel):
    capital: str = Field(description="capital of country")
    name: str = Field(description="name of country")
    population: str = Field(description="ppulation of country")
def main():
    country= input("Enter a country: ")
    llm= ChatOpenAI (openai_api_key = OPENAI_API_KEY, 
                     model_name = OPEN_AI_MODEL,
                     max_tokens=100,
                     temperature=0.7,)
    
    parser= PydanticOutputParser(pydantic_object = Country)
    message= HumanMessagePromptTemplate.from_template(
        template= PROMPT_COUNTRY_INFO )
    
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    
    chat_prompt_with_values = chat_prompt.format_prompt (
        country = country,
        format_instructions = parser.get_format_instructions()
    )
    
    response = llm (chat_prompt_with_values.to_messages())
    data= parser.parse(response.content)
    
    print(f"The capitol of {data.name} is {data.capital}." )
    print(f"The population of {data.name} is {data.population}." )

if __name__ == "__main__":
    main()     