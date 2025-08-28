from app.crewai.crewai_agent import classify_ticket
from playground.data.tickets import get_ticket_by_id
from playground.data.models import get_default_model
from playground.data.expected_classifications import get_expected_classification
from playground.evaluate_classification import evaluate_classification
from utils.logger import setup_logger
from utils.model import Model
from utils.ticket import Ticket


async def process_ticket_event(ticket_event: Ticket, model: Model) -> Ticket:
    logger = setup_logger()
    try:
        ticket_event = await classify_ticket(ticket_event, model)
    except Exception as e:
        logger.error(f"Error in process_ticket_event: {str(e)}")
    return ticket_event


async def run_crewai(ticket_id: int, model: Model = get_default_model()):
    logger = setup_logger()

    ticket_event = get_ticket_by_id(ticket_id)
    logger.info(f"{ticket_event.id}: Start processing ticket event...")

    ticket_event = await process_ticket_event(ticket_event, model)

    if ticket_event.is_classified:
        logger.debug(f"Ticket: {ticket_event.model_dump_json(indent=2)}")
        score = evaluate_classification(
            ticket_event.classification,
            get_expected_classification(ticket_id),
            ticket_event.id,
        )
        logger.info(f"{ticket_event.id}: Evaluation score: {score}")
    else:
        logger.warning(f"{ticket_event.id}: Ticket event not classified.")
        logger.info(f"{ticket_event.id}: Evaluation score: 0")
