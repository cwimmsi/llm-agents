from app.langchain.langchain_model_creator import model_creator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from prompts.ticket_prompt import get_prompt_by_version_id
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger

logger = setup_logger()


def classify_ticket(ticket: Ticket, prompt_id: int, model: Model) -> Ticket:
    prompt_template = get_prompt_by_version_id(prompt_id)
    logger.debug(f"Using prompt template: {prompt_template}")

    prompt = ChatPromptTemplate.from_template(prompt_template)

    chat_model = model_creator(model)

    parser = PydanticOutputParser(pydantic_object=TicketClassification)

    # Create chain
    chain = prompt | chat_model | parser

    # Run classification
    try:
        ticket_classification = chain.invoke(
            {
                "subject": ticket.subject,
                "body": ticket.body,
                "output_format_instructions": parser.get_format_instructions(),
            }
        )
        logger.debug(f"Ticket classification: {ticket_classification}")
        ticket.set_classification(ticket_classification)
        return ticket
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")
        raise
