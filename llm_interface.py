import os
import openai
from dotenv import load_dotenv

load_dotenv()

def call_model(prompt: str, max_tokens=3000, temperature=0.1) -> str:
    """
    Core function to call OpenAI GPT-3.5-turbo model.

    Args:
        prompt: The prompt to send to the model
        max_tokens: Maximum tokens in response
        temperature: Controls randomness (0.0-1.0)

    Returns:
        Model response as string
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message["content"]  # type: ignore
