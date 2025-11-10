"""
Story generation with adaptive prompting based on reading level.
"""
from llm_interface import call_model
from reading_diagnostic import get_level_requirements

def generate_story(user_input: str, reading_level: str = 'intermediate') -> str:
    """
    Generate a children's story adapted to reading level.
    Uses higher temperature for creative story generation.
    """
    # Get reading level-specific requirements
    level_reqs = get_level_requirements(reading_level)

    prompt = f"""You are an expert children's story writer. Create an engaging bedtime story based on the request below.

        Story Request: {user_input}

        STORY REQUIREMENTS:
        - Appropriate for children ages 5-10
        - Include dialogue to make it engaging
        - Have a clear beginning, middle, and end
        - Keep it between 300-400 words
        - Include a positive message or gentle lesson

        READING LEVEL REQUIREMENTS ({reading_level.upper()}):
        {level_reqs}

        STORY TYPE GUIDANCE:
        Determine the best story type from the request (adventure, friendship, fantasy, educational, problem-solving, bedtime, or animal tale) and write accordingly:
        - Adventures: Include challenges, excitement, and satisfying resolution
        - Friendship: Show emotions, caring, and what makes good friends
        - Fantasy: Create wonder with simple, consistent magical elements
        - Educational: Teach naturally through fun, relatable examples
        - Problem-solving: Show characters thinking through solutions creatively
        - Bedtime: Use calm, peaceful language with soothing rhythm
        - Animal tales: Give animals personality while teaching values

        Write the story now (story text only, no commentary):"""

    # Use higher temperature for creative storytelling
    story = call_model(prompt, max_tokens=1000, temperature=0.8)

    return story
