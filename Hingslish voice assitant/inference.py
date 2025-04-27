import openai
import os

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Define test prompts
prompts = [
    "Mujhe ek chai pilao.",
    "Aaj sham ko kya karu?",
    "Ek funny joke sunao."
]

# Generate responses
for prompt in prompts:
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo:your-org:your-model-id",  # Replace with your fine-tuned model ID
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=50
    )
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}\n")