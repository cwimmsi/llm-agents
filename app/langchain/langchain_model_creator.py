import os
from dotenv import load_dotenv
from langchain_ollama.chat_models import ChatOllama
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from playground.models import get_default_model
from utils.model import Model, ModelProvider
from utils.ticket import TicketClassification
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger()


def model_creator(model: Model):
    if model.provider == ModelProvider.OLLAMA:
        chat_model = ChatOllama(
            model=model.get_name_value(),
            temperature=0.2,
        )
        chat_model.with_structured_output(TicketClassification)
    elif model.provider == ModelProvider.MISTRALAI:
        chat_model = ChatMistralAI(
            api_key=os.environ.get("MISTRALAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
        chat_model.with_structured_output(TicketClassification)
    elif model.provider == ModelProvider.OPENAI:
        chat_model = ChatOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
        chat_model.with_structured_output(TicketClassification)
    elif model.provider == ModelProvider.GOOGLEGENAI:
        chat_model = ChatGoogleGenerativeAI(
            api_key=os.environ.get("GOOGLEGENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
        chat_model.with_structured_output(TicketClassification)
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        chat_model = ChatOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
        chat_model.with_structured_output(TicketClassification)

    return chat_model
