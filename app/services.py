import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def summarize_document(text:str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini" #Figure out the cheapest one to use
        messages=[{"role":"user","content": f"Summarize this: {text}"}]
    )
    return response.choices[0].message["content"]