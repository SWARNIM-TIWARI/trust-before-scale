# mock_openai.py
import random

# Context-aware mock recommendations
HIGH_RECOMMENDATIONS = [
    "Add human-in-loop review",
    "Implement privacy logging",
    "Enhance security logging"
]

MEDIUM_RECOMMENDATIONS = [
    "Add audit trail",
    "Improve monitoring",
    "Document data handling"
]

LOW_RECOMMENDATIONS = [
    "Enhance explainability dashboard",
    "Add data minimization checks",
    "Provide clear user guidance"
]

def get_recommendation(severity):
    """
    Returns a mock LLM recommendation based on feature severity.
    """
    if severity == 'High':
        return random.choice(HIGH_RECOMMENDATIONS)
    elif severity == 'Medium':
        return random.choice(MEDIUM_RECOMMENDATIONS)
    else:
        return random.choice(LOW_RECOMMENDATIONS)
