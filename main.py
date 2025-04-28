import os
from openai import OpenAI
from chatbot import *


# Initalize API Key
API_KEY = 'YOUR_API_KEY'  # Replace with your actual OpenAI API key

# Generate API KEY from OPENAI website and define as a variable.
os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize Necessary Parameters
MODEL_NAME = "gpt-3.5-turbo-16k"

INSTRUCTION = """You are intent categorizer. Base on the user's input, answer "healthcare" if the user asks about health, healthcare, diseases, or illnesses.
                        Answer "legal", if the user asks about legal.
                        Answer "education", if the user asks about education, academic, Pysics, Chemistry, Biology, Mathematics, or otherล subjects."""


# Initialize the OpenAI API client
LLM1 = OpenAI()


# Start the chat loop
chat_history = []
QUERY = None  # Initialize query to avoid potential reference error

while True:
    if not QUERY:
        QUERY = input("User: ")
    if QUERY in ['quit', 'q', 'exit']:
        break

    INTENT = intent_categorizer(query=QUERY, llm=LLM1, model_name=MODEL_NAME, instruction=INSTRUCTION)
    print("Intent:", INTENT)

    if INTENT.lower().strip() == "healthcare":
        call_admin_healthcare()
        break
    elif INTENT.lower().strip() == "legal":
        call_admin_legal()
        break
    elif INTENT.lower().strip() == "education":
        call_admin_education()
        break
    else:
        call_admin_others()
        break

    query = None
    