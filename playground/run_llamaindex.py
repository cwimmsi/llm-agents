import asyncio
from app.llamaindex.llamaindex_agent import classify_ticket
from playground.tickets import get_ticket_by_id
from playground.models import get_default_model
from utils.logger import setup_logger
from utils.model import Model
from utils.ticket import Ticket

logger = setup_logger()


def process_ticket_event(ticket_event: Ticket, prompt_id: int, model: Model) -> Ticket:
    try:
        ticket_event = asyncio.run(classify_ticket(ticket_event, prompt_id, model))
        return ticket_event
    except Exception as e:
        logger.error(f"Error in process_ticket_event: {str(e)}")
        raise


def run_llamaindex(
    ticket_id: int, prompt_id: int = 1, model: Model = get_default_model()
):
    ticket_event = get_ticket_by_id(ticket_id)
    logger.info(f"LLAMAINDEX: Processing ticket event: {ticket_event.id}")
    logger.info(f"LLAMAINDEX: Using model: {model.provider} - {model.name}")

    ticket_event = process_ticket_event(ticket_event, prompt_id, model)
    if ticket_event:
        logger.info(f"LLAMAINDEX: {ticket_event.model_dump_json(indent=2)}")

    logger.info(f"LLAMAINDEX: Ticket processing completed.")
