from app.langchain.langchain_model_creator import model_creator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from prompts.format_instructions_prompt import get_format_instructions_prompt
from prompts.system_prompt import get_system_prompt
from prompts.user_prompt import get_user_prompt
from utils.model import Model
from utils.ticket import Ticket, TicketClassification
from utils.logger import setup_logger


async def classify_ticket(ticket: Ticket, model: Model) -> Ticket:
    logger = setup_logger()

    system_prompt = get_system_prompt()
    system_prompt = f"{system_prompt}\n\n{get_format_instructions_prompt()}"
    user_prompt = get_user_prompt()

    logger.debug(f"Using system prompt template: {system_prompt}")
    logger.debug(f"Using user prompt template: {user_prompt}")

    parser = PydanticOutputParser(pydantic_object=TicketClassification)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", user_prompt),
        ]
    ).partial(output_format_instructions=parser.get_format_instructions())

    llm = model_creator(model)
    llm.with_structured_output(TicketClassification)

    # Create chain
    chain = prompt | llm | parser

    try:
        # use asynchronous call
        ticket_classification = await chain.ainvoke(
            {"subject": ticket.subject, "body": ticket.body}
        )
        logger.debug(f"Ticket classification: {ticket_classification}")
        # set classification on ticket object
        ticket.set_classification(ticket_classification)
    except Exception as e:
        logger.error(f"Error in classify_ticket: {str(e)}")

    return ticket
