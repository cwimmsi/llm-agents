from agents import Agent, Runner, ModelSettings
from app.openai.openai_model_creator import model_creator
from prompts.ticket_prompt import get_prompt_by_version_id
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

logger = setup_logger()


def classify_ticket(ticket: Ticket, prompt_id: int, model: Model) -> Ticket:
    prompt_template = get_prompt_by_version_id(prompt_id)
    logger.debug(f"Using prompt template: {prompt_template}")

    prompt = prompt_template.format(
        subject=ticket.subject, body=ticket.body, output_format_instructions=""
    )

    llm = model_creator(model)

    agent = Agent(
        name="ticket_classifier",
        instructions=prompt,
        output_type=TicketClassification,
        model=llm,
        model_settings=ModelSettings(temperature=0.1),
    )

    try:
        response = Runner.run_sync(agent, "")
        ticket_classification = response.final_output
        logger.debug(f"Ticket classification: {ticket_classification}")

        ticket.set_classification(ticket_classification)
        return ticket
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")
        raise
