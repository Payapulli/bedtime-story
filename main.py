"""
Bedtime Story Generator - Main Orchestration

A multi-agent system that generates age-appropriate bedtime stories for children
ages 5-10 using category-specific prompting and LLM-based quality evaluation.

Before submitting the assignment, describe here in a few sentences what you would
have built next if you spent 2 more hours on this project:

If I had 2 more hours, I would add: (1) Interactive story branching where children
can choose "what happens next" from 2-3 options and the system generates a
continuation based on their choice, (2) a story series/chapter system that maintains
character and plot continuity across multiple sessions (e.g., "Day 1 of the adventure",
"Day 2", etc.), and (3) the ability to save favorite characters/settings to a profile
so children can request new stories featuring their beloved characters across different
adventures, creating a personalized story universe.
"""

from validators import is_input_detailed_enough, check_content_safety
from generator import generate_story
from judge import judge_story
from refiner import refine_story
from reading_diagnostic import administer_diagnostic

def main():
    """Main orchestration for bedtime story generation with quality control."""
    print("----- Bedtime Story Generator -----n")

    reading_level = administer_diagnostic()

    user_input = input("\nWhat kind of story do you want to hear? ")

    # Validate if input is detailed enough
    if not is_input_detailed_enough(user_input):
        print("\nHmm, that's a bit vague! Can you tell me more?")
        print("For example: 'A story about a brave knight and a friendly dragon'")
        additional_input = input("\nWhat kind of story would you like? ")
        user_input = additional_input

    # Check content safety
    print("\n[Checking content safety...]")
    safety_check = check_content_safety(user_input)

    if not safety_check.get("safe", True):
        reason = safety_check.get("reason", "inappropriate content")
        print(f"\nSorry, I can't create that story: {reason}")
        print("\nPlease request a different story that's appropriate for children ages 5-10.")
        print("Examples: adventures, friendship, animals, fantasy, problem-solving, etc.")
        return

    # Generate story with reading level adaptation
    print("\n[Generating your story...]\n")
    story = generate_story(user_input, reading_level)

    # Judge the story
    print("[Evaluating story quality...]\n")
    evaluation = judge_story(story, user_input)

    overall_score = evaluation.get("overall_score", 0)
    verdict = evaluation.get("verdict", "PASS")

    print(f"[Judge Score: {overall_score:.1f}/10]")
    print(f"[Verdict: {verdict}]\n")

    # Refine if needed
    final_story = story
    if verdict == "NEEDS_IMPROVEMENT":
        print("[Story needs improvement. Refining...]\n")
        final_story = refine_story(story, evaluation, user_input)
        print("[Refinement complete!]\n")
    else:
        print("[Story passed quality check!]\n")

    # Display final story
    print("=" * 60)
    print("YOUR BEDTIME STORY")
    print("=" * 60)
    print(final_story)
    print("=" * 60)

if __name__ == "__main__":
    main()