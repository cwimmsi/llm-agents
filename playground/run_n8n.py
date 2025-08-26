import requests
from prompts.ticket_prompt import get_prompt_by_version_id
from utils.logger import setup_logger
from utils.ticket import Ticket, TicketClassification
from playground.tickets import get_ticket_by_id


N8N_WEBHOOK_URL_TEST = (
    "http://localhost:5678/webhook-test/14be3ed3-a7e9-4948-a5c2-9f4b464e3c1b"
)
N8N_WEBHOOK_URL_PROD = (
    "http://localhost:5678/webhook/14be3ed3-a7e9-4948-a5c2-9f4b464e3c1b"
)

logger = setup_logger()


def process_ticket_event(ticket_event: Ticket, n8n_webhook_url: str) -> Ticket:
    try:
        response = requests.post(n8n_webhook_url, json=ticket_event.model_dump())
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        logger.debug(f"Response status code: {response.status_code}")

        # Parse into TicketClassification object
        ticket_classification = TicketClassification(
            **response.json().get("classification")
        )
        if ticket_classification:
            ticket_event.set_classification(ticket_classification)

        return ticket_event
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending event to n8n: {str(e)}")
        raise


def trigger_n8n_endpoint(ticket_id: int, n8n_webhook_url: str):
    ticket_event = get_ticket_by_id(ticket_id)
    logger.info(f"N8N: Processing ticket event: {ticket_event.id}")
    # logger.info(f"N8N: Using model: {model.provider} - {model.name}")

    ticket_event = process_ticket_event(ticket_event, n8n_webhook_url)
    if ticket_event:
        logger.info(f"N8N: {ticket_event.model_dump_json(indent=2)}")

    logger.info(f"N8N: Ticket processing completed.")


def run_n8n_endpoint_test(ticket_id: int):
    trigger_n8n_endpoint(ticket_id, N8N_WEBHOOK_URL_TEST)


def run_n8n_endpoint_prod(ticket_id: int):
    trigger_n8n_endpoint(ticket_id, N8N_WEBHOOK_URL_PROD)
