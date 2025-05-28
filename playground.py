import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Collect input parameters
system_prompt = input("Enter system prompt (e.g., 'Answer concisely'): ").strip()

user_prompt = input("Enter your prompt (e.g., 'Capital of France?'): ").strip()

model = input("Enter model (gpt-3.5-turbo or gpt-4o): ").strip()
if model not in ["gpt-3.5-turbo", "gpt-4o"]:
    raise ValueError("Invalid model selected. Choose 'gpt-3.5-turbo' or 'gpt-4o'.")

temperature = float(input("Enter temperature (0.0 to 1.5): "))
if not (0.0 <= temperature <= 1.5):
    raise ValueError("Temperature must be between 0.0 and 1.5.")

max_tokens = int(input("Enter max tokens (10 to 300): "))
if not (10 <= max_tokens <= 300):
    raise ValueError("Max tokens must be between 10 and 300.")

frequency_penalty = float(input("Enter frequency penalty (0.0 to 2.0): "))
if not (0.0 <= frequency_penalty <= 2.0):
    raise ValueError("Frequency penalty must be between 0.0 and 2.0.")

presence_penalty = float(input("Enter presence penalty (0.0 to 2.0): "))
if not (0.0 <= presence_penalty <= 2.0):
    raise ValueError("Presence penalty must be between 0.0 and 2.0.")

stop_input = input("Enter stop sequence(s) separated by commas (or leave empty): ").strip()
stop = [s.strip() for s in stop_input.split(",")] if stop_input else None

# Call OpenAI API
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    stop=stop
)

# Extract and print response
answer = response.choices[0].message.content
tokens_used = response.usage

print("\nUser Settings:\n--------------")
print(f"System Prompt: {system_prompt}")
print(f"User Prompt: {user_prompt}")
print(f"Model: {model}")
print(f"Temperature: {temperature}")
print(f"Max Tokens: {max_tokens}")
print(f"Frequency Penalty: {frequency_penalty}")
print(f"Presence Penalty: {presence_penalty}")
print(f"Stop Sequence: {stop if stop else 'None'}")

print("\nAssistant's Response:\n----------------------")
print(answer)
