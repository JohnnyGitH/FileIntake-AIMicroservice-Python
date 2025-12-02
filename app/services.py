import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("Key_Goes_here"))

async def summarize_document(prompt:str) -> str:
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini", #Figure out the cheapest one to use
    #     messages=[
    #         {"role":"system","content": "You are a helpful assistant"}, # Context
    #         {"role":"user","content": f"Summarize this: {prompt}"} # prompt
    #     ],
    # )

    # reply = response.choices[0].message.content
    # print(reply)

    # return reply or ""

    if not prompt:
        return "No Content Available"
    
    return "This is a sample AI response. The Service is connected BEEP BOOP"