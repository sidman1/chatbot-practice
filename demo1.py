import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPEN_AI_MODEL = "gpt-3.5-turbo"

def main():
    llm= ChatOpenAI (openai_api_key = OPENAI_API_KEY, 
                     model_name = OPEN_AI_MODEL,
                     max_tokens=100,
                     temperature=0.7,)
    result= llm.predict("Give me 5 youtube video ideas",
                        max_tokens=100)
    print(result)  

if __name__ == "__main__":
    main()            