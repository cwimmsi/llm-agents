"""Used for formatting output in langchain app."""

OUTPUT_FORMAT_INSTRUCTIONS = """
## Output format instructions
{{output_format_instructions}}
"""


def get_format_instructions_prompt() -> str:
    """Get the format instructions prompt."""
    return OUTPUT_FORMAT_INSTRUCTIONS
