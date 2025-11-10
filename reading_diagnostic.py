"""
Reading level selection based on grade input.
"""

def administer_diagnostic() -> str:
    """
    Ask for the child's grade and map to reading level.
    Returns reading level: 'beginner', 'intermediate', or 'advanced'
    """
    print("What grade is your child in? (K-5)")
    print("  K-1: Beginner level (simple words, short sentences)")
    print("  2-3: Intermediate level (balanced vocabulary)")
    print("  4-5: Advanced level (richer vocabulary)")

    grade_input = input("\nGrade (or press Enter to skip): ").strip().upper()

    # Default to intermediate if skipped
    if not grade_input:
        print("[Using default: Intermediate level]\n")
        return 'intermediate'

    # Map grade to reading level
    if grade_input in ['K', 'KINDERGARTEN', '1', 'FIRST']:
        level = 'beginner'
        print(f"[Reading Level: Beginner - simple vocabulary]\n")
    elif grade_input in ['2', 'SECOND', '3', 'THIRD']:
        level = 'intermediate'
        print(f"[Reading Level: Intermediate - balanced vocabulary]\n")
    elif grade_input in ['4', 'FOURTH', '5', 'FIFTH']:
        level = 'advanced'
        print(f"[Reading Level: Advanced - rich vocabulary]\n")
    else:
        # Default to intermediate for any unrecognized input
        level = 'intermediate'
        print(f"[Using default: Intermediate level]\n")

    return level


def get_level_requirements(reading_level: str) -> str:
    """
    Return language requirements based on reading level.
    """
    level_requirements = {
        'beginner': (
            "- Use very simple vocabulary (mostly 1-2 syllable words)\n"
            "- Keep sentences short (5-10 words)\n"
            "- Use common, everyday words\n"
            "- Avoid complex sentence structures\n"
            "- Include 2-3 slightly challenging words with clear context clues"
        ),
        'intermediate': (
            "- Use clear language with some variety\n"
            "- Mix simple and moderate sentence lengths\n"
            "- Include 3-4 vocabulary builder words (explained through context)\n"
            "- Use some descriptive adjectives and adverbs\n"
            "- Balance familiar and slightly challenging words"
        ),
        'advanced': (
            "- Use richer, more varied vocabulary\n"
            "- Include 4-5 advanced vocabulary words with context clues\n"
            "- Use more complex sentence structures (but still age-appropriate)\n"
            "- Include descriptive language and figurative expressions\n"
            "- Challenge the reader while remaining accessible"
        )
    }

    return level_requirements.get(reading_level, level_requirements['intermediate'])
