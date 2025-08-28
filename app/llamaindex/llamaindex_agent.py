from app.llamaindex.llamaindex_model_creator import model_creator
from llama_index.core.agent.workflow import FunctionAgent
from prompts.system_prompt import get_system_prompt
from prompts.user_prompt import get_user_prompt
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger


async def classify_ticket(ticket: Ticket, model: Model) -> Ticket:
    logger = setup_logger()

    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt()
    user_prompt = user_prompt.format(subject=ticket.subject, body=ticket.body)

    logger.debug(f"Using system prompt template: {system_prompt}")
    logger.debug(f"Using user prompt template: {user_prompt}")

    llm = model_creator(model)

    agent = FunctionAgent(
        name="Ticket Classification agent",
        system_prompt=system_prompt,
        llm=llm,
        output_cls=TicketClassification,
    )

    try:
        # use asynchronous call
        response = await agent.run(user_msg=user_prompt)
        # retrieve ticket classification object
        ticket_classification = response.get_pydantic_model(TicketClassification)
        logger.debug(f"Ticket classification: {ticket_classification}")
        # set classification on ticket object
        ticket.set_classification(ticket_classification)
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")

    return ticket
