import asyncio
from app.openai.openai_agent import classify_ticket
from playground.tickets import get_ticket_by_id
from playground.models import get_default_model
from utils.logger import setup_logger
from utils.model import Model
from utils.ticket import Ticket

logger = setup_logger()


def process_ticket_event(ticket_event: Ticket, model: Model) -> Ticket:
    try:
        ticket_event = asyncio.run(classify_ticket(ticket_event, model))
    except Exception as e:
        logger.error(f"Error in process_ticket_event: {str(e)}")
    return ticket_event


def run_openai(ticket_id: int, model: Model = get_default_model()):
    ticket_event = get_ticket_by_id(ticket_id)
    logger.info(f"OPENAISDK: Processing ticket event: {ticket_event.id}")
    logger.info(
        f"OPENAISDK: Using model: {model.get_provider_value()}/{model.get_name_value()}"
    )

    ticket_event = process_ticket_event(ticket_event, model)
    if ticket_event.is_classified:
        logger.info(f"OPENAISDK: {ticket_event.model_dump_json(indent=2)}")
    else:
        logger.warning(f"OPENAISDK: Ticket event not classified.")

    logger.info(f"OPENAISDK: Ticket processing completed.")
