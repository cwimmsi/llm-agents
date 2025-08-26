from app.pydanticai.pydanticai_model_creator import model_creator
from prompts.ticket_prompt import get_prompt_by_version_id
from pydantic_ai import Agent
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

logger = setup_logger()


def classify_ticket(ticket: Ticket, prompt_id: int, model: Model) -> Ticket:
    prompt_template = get_prompt_by_version_id(prompt_id)
    logger.debug(f"Using prompt template: {prompt_template}")

    system_prompt = prompt_template.format(
        subject=ticket.subject, body=ticket.body, output_format_instructions=""
    )

    llm = model_creator(model)

    agent = Agent(
        model=llm, system_prompt=system_prompt, output_type=TicketClassification
    )

    try:
        response = agent.run_sync(user_prompt="")
        ticket_classification = response.output
        logger.debug(f"Ticket classification: {ticket_classification}")
        ticket.set_classification(ticket_classification)
        return ticket
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")
        raise
