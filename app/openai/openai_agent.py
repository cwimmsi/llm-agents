from agents import Agent, Runner, ModelSettings
from app.openai.openai_model_creator import model_creator
from prompts.system_prompt import get_system_prompt
from prompts.user_prompt import get_user_prompt
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

logger = setup_logger()


async def classify_ticket(ticket: Ticket, model: Model) -> Ticket:
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt()
    user_prompt = user_prompt.format(subject=ticket.subject, body=ticket.body)

    logger.debug(f"Using system prompt template: {system_prompt}")
    logger.debug(f"Using user prompt template: {user_prompt}")

    llm = model_creator(model)

    agent = Agent(
        name="Ticket classifier agent",
        model=llm,
        model_settings=ModelSettings(temperature=0.0),
        instructions=system_prompt,
        output_type=TicketClassification,
    )

    try:
        # use asynchronous call
        response = await Runner.run(agent, user_prompt)
        # retrieve ticket classification object
        ticket_classification = response.final_output
        logger.debug(f"Ticket classification: {ticket_classification}")
        # set classification on ticket object
        ticket.set_classification(ticket_classification)
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")

    return ticket
