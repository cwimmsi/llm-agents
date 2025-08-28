from typing import Dict

USER_PROMPT: Dict[int, str] = {
    1: f"""
## Input
Analyse the following ticket and perform the classification tasks:
Ticket subject: {{subject}}
Ticket body: {{body}}
"""
}


def get_user_prompt(version_id: int = 1) -> str:
    """Get user prompt by its version id."""
    if version_id not in USER_PROMPT:
        raise ValueError(f"User prompt version ID {version_id} not recognized.")
    return USER_PROMPT[version_id]
