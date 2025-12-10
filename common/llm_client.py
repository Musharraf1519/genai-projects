# common/llm_client.py
# Simple wrapper for OpenAI client; extend as needed for retries, logging, and providers.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_KEY)

def chat_completion(messages, model='gpt-4.1-mini', temperature=0.3, max_tokens=400):
    """Wrapper: returns response object from OpenAI client."""
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
