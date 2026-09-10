import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("🤖 My Personal AI Agent is running!")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Agent: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=user_input
    )

    print("Agent:", response.output_text)
