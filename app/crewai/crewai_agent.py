from app.crewai.crewai_model_creator import model_creator
from crewai import Agent
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
        role="IT Help Desk Ticket Classifier",
        goal="Accurately classify incoming IT help desk tickets into predefined categories to streamline the support process and improve response times.",
        backstory=prompt,
        llm=llm,
    )

    try:
        response = agent.kickoff(
            "Classify the ticket", response_format=TicketClassification
        )
        ticket_classification = response.pydantic
        logger.debug(f"Ticket classification: {ticket_classification}")
        ticket.set_classification(ticket_classification)
        return ticket
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")
        raise
