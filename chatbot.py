import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPEN_AI_MODEL = "gpt-3.5-turbo"
openai_api_key = os.getenv("OPENAI_API_KEY")

template = """
You are an AI mental health counselor and crisis counselor \
You are chatting with someone who might be having a mental \
health crisis or suicidal thoughts. 
{chat_history}
Human: {human_input}
"""

prompt = PromptTemplate(
    input_variables = ["chat_history", "human_input"], template = template)
memory = ConversationBufferMemory(memory_key = "chat_history")

llm = ChatOpenAI(openai_api_key= openai_api_key, model_name = OPEN_AI_MODEL)

chat_llm_chain = LLMChain (
    llm=llm,
    prompt=prompt,
    verbose=False,
    memory=memory
)

human= input ("How may I assist you? \n Type exit to end the conversation \n Enter response: ")
while human !="exit":
    response= chat_llm_chain.predict(human_input=human)
    print(response + "\n Type exit to end the conversation")
    human= input ("Enter a response: ")
