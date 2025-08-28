import httpx
from playground.data.tickets import get_ticket_by_id
from playground.data.models import get_default_model
from playground.data.expected_classifications import get_expected_classification
from playground.evaluate_classification import evaluate_classification
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

N8N_WEBHOOK_URL_TEST = (
    "http://localhost:5678/webhook-test/14be3ed3-a7e9-4948-a5c2-9f4b464e3c1b"
)
N8N_WEBHOOK_URL_PROD = (
    "http://localhost:5678/webhook/14be3ed3-a7e9-4948-a5c2-9f4b464e3c1b"
)


async def process_ticket_event(ticket_event: Ticket, n8n_webhook_url: str) -> Ticket:
    logger = setup_logger()
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                n8n_webhook_url, json=ticket_event.model_dump()
            )
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
            logger.debug(f"Response status code: {response.status_code}")

            # Parse into TicketClassification object
            ticket_classification = TicketClassification(
                **response.json().get("classification")
            )
            if ticket_classification:
                ticket_event.set_classification(ticket_classification)

        except httpx.RequestError as e:
            logger.error(f"Error sending event to n8n: {str(e)}")

    return ticket_event


async def trigger_n8n_endpoint(ticket_id: int, n8n_webhook_url: str):
    logger = setup_logger()

    ticket_event = get_ticket_by_id(ticket_id)
    logger.info(f"{ticket_event.id}: Start processing ticket event...")

    ticket_event = await process_ticket_event(ticket_event, n8n_webhook_url)
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


async def run_n8n_test(ticket_id: int, model: Model = get_default_model()):
    # Model gets set inside n8n workflow and can't be changed via the trigger
    await trigger_n8n_endpoint(ticket_id, N8N_WEBHOOK_URL_TEST)


async def run_n8n(ticket_id: int, model: Model = get_default_model()):
    # Model gets set inside n8n workflow and can't be changed via the trigger
    await trigger_n8n_endpoint(ticket_id, N8N_WEBHOOK_URL_PROD)
