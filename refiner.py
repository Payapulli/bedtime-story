"""
Story refinement based on judge feedback.
"""
from llm_interface import call_model

def refine_story(original_story: str, evaluation: dict, user_input: str) -> str:
    """
    Refine the story based on judge feedback.
    Uses lower temperature for more controlled improvements.
    """
    improvements = evaluation.get("improvements", [])
    improvements_text = "\n".join([f"- {imp}" for imp in improvements])

    refine_prompt = f"""You are a children's story editor. Improve this story based on specific feedback.

    Original Story Request: {user_input}

    CURRENT STORY:
    {original_story}

    FEEDBACK TO ADDRESS:
    {improvements_text}

    Your task:
    1. Keep the core plot and characters the same
    2. Address each piece of feedback specifically
    3. Maintain appropriate length (300-400 words)
    4. Keep it age-appropriate for children 5-10

    Write the IMPROVED story now (do not include any commentary, just the story):"""

    refined_story = call_model(refine_prompt, max_tokens=1000, temperature=0.6)

    return refined_story
