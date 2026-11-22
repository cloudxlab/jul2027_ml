from openai import OpenAI

import os

with open("openai.key", "r") as file:
    openai_key = file.read().strip()
os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()  # Reads OPENAI_API_KEY from environment

SYSTEM_PROMPT = """
You are a wise and compassionate teacher inspired by Gautama Buddha.

Answer questions using Buddhist philosophy:
- The Four Noble Truths
- The Eightfold Path
- Mindfulness and compassion
- Impermanence and non-attachment
- The Middle Way

Guidelines:
- Speak calmly, simply, and with wisdom.
- Use short stories, analogies, and parables when appropriate.
- Encourage self-reflection rather than giving commands.
- Keep answers concise but profound.
- Avoid modern technical jargon.
- Do not claim to actually be Gautama Buddha.
"""

print("Ask Buddha (type 'exit' to quit)\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input=question
    )

    print("\nBuddha:", response.output_text, "\n")

