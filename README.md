# Bedtime Story Generator

A multi-agent AI system that generates age-appropriate bedtime stories for children ages 5-10 using adaptive prompting, LLM-based quality evaluation, and iterative refinement.

## Architecture

This system uses a **5-stage pipeline** with multiple specialized agents:

```
User Input → Validation → Generation → Evaluation → Refinement → Final Story
```

### System Flow

1. **Reading Level Diagnostic** ([reading_diagnostic.py](reading_diagnostic.py))
   - Assesses child's grade level (K-5)
   - Maps to reading level: beginner, intermediate, or advanced
   - Adapts vocabulary and sentence complexity

2. **Input Validation** ([validators.py](validators.py))
   - **Detail Check**: Ensures request has sufficient detail (≥5 words)
   - **Content Safety**: LLM-based safety filter checks for inappropriate topics
   - Rejects unsafe content (violence, scary themes, adult content, etc.)

3. **Story Generation** ([generator.py](generator.py))
   - Generates 300-400 word stories adapted to reading level
   - Uses **category-specific prompting** (adventure, friendship, fantasy, educational, problem-solving, bedtime, animal tales)
   - Higher temperature (0.8) for creative storytelling
   - Incorporates reading level requirements into prompt

4. **LLM Judge Evaluation** ([judge.py](judge.py))
   - Evaluates story across **8 criteria**:
     - Age-appropriateness
     - Language clarity
     - Story structure
     - Engagement
     - Positive message
     - Dialogue quality
     - Creativity
     - Emotional resonance
   - Returns structured JSON with scores, strengths, and improvements
   - **Verdict**: PASS (≥7.5/10) or NEEDS_IMPROVEMENT (<7.5/10)

5. **Story Refinement** ([refiner.py](refiner.py))
   - Triggered if verdict is NEEDS_IMPROVEMENT
   - Takes judge feedback and refines story
   - Maintains core plot while addressing specific critiques
   - Lower temperature (0.6) for controlled improvements

## Setup

### Prerequisites
- Python 3.7+
- OpenAI API key

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd bedtime-story
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up OpenAI API key**

Create a `.env` file in the project root:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Replace `your-api-key-here` with your actual OpenAI API key.

## Usage

Run the story generator:
```bash
python main.py
```

## Key Features

- **Adaptive Reading Levels**: Automatically adjusts vocabulary and sentence complexity
- **Content Safety**: LLM-powered safety filter for age-appropriate content
- **Multi-Agent System**: Specialized components for generation, evaluation, and refinement
- **Category-Specific Prompting**: Tailored story generation based on request type
- **Quality Assurance**: 8-criterion evaluation with automatic refinement
- **Structured Feedback**: Detailed scoring and improvement suggestions

## Technical Details

- **Model**: GPT-3.5-turbo
- **Temperature Settings**:
  - Generation: 0.8 (creative)
  - Refinement: 0.6 (controlled)
  - Evaluation: 0.2 (consistent)
  - Safety: 0.1 (strict)
- **Story Length**: 300-400 words
- **Age Range**: 5-10 years old