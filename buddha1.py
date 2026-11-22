from openai import OpenAI
import tiktoken

import os

with open("openai.key", "r") as file:
    openai_key = file.read().strip()
os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

MODEL = "gpt-4.1-mini"
MAX_HISTORY_TOKENS = 2000
KEEP_LAST = 4  # Keep last 4 messages uncompressed

SYSTEM_PROMPT = """
You are a wise and compassionate teacher inspired by Gautama Buddha.
Answer questions using Buddhist philosophy.
Speak calmly, simply, and with wisdom.
Use short parables when appropriate.
"""

encoding = tiktoken.get_encoding("o200k_base")

def count_tokens(messages):
    text = "\n".join(m["content"] for m in messages)
    return len(encoding.encode(text))


def compress_history(history):
    """Summarize older messages while keeping recent messages."""

    if len(history) <= KEEP_LAST:
        return history

    old_messages = history[:-KEEP_LAST]
    recent_messages = history[-KEEP_LAST:]

    print("\n[Compressing conversation history...]")

    response = client.responses.create(
        model=MODEL,
        instructions="""
        Summarize this conversation concisely.
        Preserve:
        - Important facts about the user
        - User preferences and goals
        - Key questions and answers
        - Important context needed for future replies

        If an earlier summary exists, incorporate it.
        Do not invent information.
        """,
        input=old_messages
    )

    summary = response.output_text

    compressed = [
        {
            "role": "developer",
            "content": "Summary of earlier conversation:\n" + summary
        }
    ] + recent_messages

    print("Tokens before:", count_tokens(history))
    print("Tokens after:", count_tokens(compressed))

    return compressed


history = []

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    history.append({
        "role": "user",
        "content": question
    })

    # Compress before sending to the model
    if count_tokens(history) > MAX_HISTORY_TOKENS:
        history = compress_history(history)

    print("\n========== FULL PROMPT ==========")
    print(SYSTEM_PROMPT)
    for message in history:
        print(message["role"], ":", message["content"])

    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=history
    )

    answer = response.output_text

    print("\nBuddha:", answer)

    history.append({
        "role": "assistant",
        "content": answer
    })

    print("\n========== TOKEN USAGE ==========")
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    print("Total tokens:", response.usage.total_tokens)
    print("History tokens:", count_tokens(history))
