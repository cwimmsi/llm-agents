import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.llms.mistralai import MistralAI
from llama_index.llms.ollama import Ollama
from llama_index.llms.google_genai import GoogleGenAI
from playground.models import get_default_model
from utils.model import Model, ModelProvider
from utils.ticket import TicketClassification
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger()


def model_creator(model: Model):
    if model.provider == ModelProvider.OLLAMA:
        llm = Ollama(
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
    elif model.provider == ModelProvider.MISTRALAI:
        llm = MistralAI(
            api_key=os.environ.get("MISTRALAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
    elif model.provider == ModelProvider.OPENAI:
        llm = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
    elif model.provider == ModelProvider.GOOGLEGENAI:
        llm = GoogleGenAI(
            api_key=os.environ.get("GOOGLEGENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        llm = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=0.2,
            max_retries=1,
        )

    return llm
