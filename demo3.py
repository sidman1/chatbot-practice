import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.chains.api import open_meteo_docs
from langchain.chains import APIChain

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPEN_AI_MODEL = "gpt-3.5-turbo"

def main():
    llm= ChatOpenAI (openai_api_key = OPENAI_API_KEY, model_name = OPEN_AI_MODEL)
    
    location = input("Enter a location: ")
    
    chain_new = APIChain.from_llm_and_api_docs(
        llm, open_meteo_docs.OPEN_METEO_DOCS, verbose= False
    )
    
    result = chain_new.run(
        f"What is the weather at {location} in degrees Farenheight?"
    )
    print(result)
    

if __name__ == "__main__":
    main()