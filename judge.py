"""
Story evaluation with category-specific criteria.
"""
import json
from llm_interface import call_model

def judge_story(story: str, user_input: str) -> dict:
    """
    Evaluate the story using an LLM judge with comprehensive criteria.
    Returns structured feedback with scores and suggestions.
    """
    # Build the judge prompt with proper formatting
    judge_prompt = f"""You are an expert children's story critic and educator. Evaluate this bedtime story.

    Original Request: {user_input}

    STORY TO EVALUATE:
    {story}

    EVALUATION CRITERIA:
    1. Age-Appropriateness (1-10): Is the content suitable for children ages 5-10?
    2. Language Clarity (1-10): Is the language simple and easy to understand?
    3. Story Structure (1-10): Does it have a clear beginning, middle, and end?
    4. Engagement (1-10): Is it interesting and engaging for children?
    5. Positive Message (1-10): Does it include a positive lesson or message?
    6. Dialogue Quality (1-10): Is dialogue natural and age-appropriate?
    7. Creativity (1-10): Is the story imaginative and original?
    8. Emotional Resonance (1-10): Will it connect with children emotionally?

    Return ONLY a JSON object with this structure:
    {{
        "scores": {{
            "age_appropriateness": <score 1-10>,
            "language_clarity": <score 1-10>,
            "story_structure": <score 1-10>,
            "engagement": <score 1-10>,
            "positive_message": <score 1-10>,
            "dialogue_quality": <score 1-10>,
            "creativity": <score 1-10>,
            "emotional_resonance": <score 1-10>
        }},
        "overall_score": <average of all scores>,
        "strengths": ["strength 1", "strength 2"],
        "improvements": ["specific suggestion 1", "specific suggestion 2"],
        "verdict": "PASS" or "NEEDS_IMPROVEMENT"
    }}

    Verdict should be "PASS" if overall_score >= 7.5, otherwise "NEEDS_IMPROVEMENT".
    Return ONLY valid JSON, no other text."""

    response = call_model(judge_prompt, max_tokens=800, temperature=0.2)

    # Parse JSON response
    start_idx = response.find('{')
    end_idx = response.rfind('}') + 1
    json_str = response[start_idx:end_idx]
    evaluation = json.loads(json_str)
    return evaluation
