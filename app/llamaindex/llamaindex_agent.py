from app.llamaindex.llamaindex_model_creator import model_creator
from llama_index.core.prompts import PromptTemplate
from llama_index.core.agent.workflow import FunctionAgent
from prompts.ticket_prompt import get_prompt_by_version_id
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

logger = setup_logger()


async def classify_ticket(ticket: Ticket, prompt_id: int, model: Model) -> Ticket:
    prompt_template = get_prompt_by_version_id(prompt_id)
    logger.debug(f"Using prompt template: {prompt_template}")

    prompt = PromptTemplate(template=prompt_template)
    system_prompt = prompt.format(
        subject=ticket.subject,
        body=ticket.body,
        output_format_instructions="",
    )

    llm = model_creator(model)

    agent = FunctionAgent(
        name="Ticket Classification Agent",
        system_prompt=system_prompt,
        llm=llm,
        output_cls=TicketClassification,
    )

    try:
        response = await agent.run(user_msg="")
        ticket_classification = response.get_pydantic_model(TicketClassification)
        logger.debug(f"Ticket classification: {ticket_classification}")
        ticket.set_classification(ticket_classification)
        return ticket
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")
        raise
