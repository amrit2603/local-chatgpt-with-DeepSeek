import chainlit as cl
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ],
    )

    msg = cl.Message(content="")

    start_message = "Hello, I'm your 100% local alternative to ChatGPT running on DeepSeek-R1 made by Amrit kumar❤️. How can I help you today?"

    for token in start_message:
        await msg.stream_token(token)

    await msg.send()

@cl.step(type="tool")
async def tool(input_message):

    interaction = cl.user_session.get("interaction")

    interaction.append({
        "role": "user",
        "content": input_message
    })

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=interaction
    )

    assistant_reply = response.choices[0].message.content

    interaction.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply

@cl.on_message 
async def main(message: cl.Message):

    tool_res = await tool(message.content)

    msg = cl.Message(content="")
    for token in tool_res.message.content:
        await msg.stream_token(token)
        
    await msg.send()