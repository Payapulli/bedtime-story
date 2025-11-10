"""
Input validation and content safety checking.
"""
import json
from llm_interface import call_model

def is_input_detailed_enough(user_input: str) -> bool:
    """
    Check if user input has enough detail to generate a story.
    """
    MIN_WORD_THRESHOLD = 5
    word_count = len(user_input.split())
    return word_count >= MIN_WORD_THRESHOLD


def check_content_safety(user_input: str) -> dict:
    """
    Check if the user's request contains inappropriate content for children's stories.
    Returns dict with 'safe' boolean and 'reason' if unsafe.
    """
    safety_prompt = f"""You are a content safety filter for a children's story generator (ages 5-10).

    Analyze this story request and determine if it's appropriate:

    Request: "{user_input}"

    UNSAFE topics include:
    - Violence, gore, death, or harm
    - Sexual content or abuse of any kind
    - Scary/horror themes
    - Inappropriate language or slurs
    - Discrimination or hate
    - Drugs, alcohol, or adult themes
    - Dangerous activities that could be imitated
    - Political content or controversial topics

    Return ONLY a JSON object:
    {{
        "safe": true or false,
        "reason": "brief explanation if unsafe, empty string if safe"
    }}

    Be strict - err on the side of caution for children's safety.
    Return ONLY valid JSON, no other text."""

    response = call_model(safety_prompt, max_tokens=150, temperature=0.1)

    start_idx = response.find('{')
    end_idx = response.rfind('}') + 1
    json_str = response[start_idx:end_idx]
    safety_check = json.loads(json_str)
    return safety_check
