import os
from dotenv import load_dotenv
from agents.extensions.models.litellm_model import LitellmModel
from playground.models import get_default_model
from utils.model import Model, ModelProvider
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger()


def model_creator(model: Model):
    if model.provider == ModelProvider.OLLAMA:
        llm = LitellmModel(
            model=f"ollama/{model.get_name_value()}",
            base_url="http://localhost:11434",
        )
    elif model.provider == ModelProvider.MISTRALAI:
        llm = LitellmModel(
            model=f"mistral/{model.get_name_value()}",
            api_key=os.environ.get("MISTRALAI_API_KEY"),
        )
    elif model.provider == ModelProvider.OPENAI:
        llm = LitellmModel(
            model=f"openai/{model.get_name_value()}",
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
    elif model.provider == ModelProvider.GOOGLEGENAI:
        llm = LitellmModel(
            model=f"gemini/{model.get_name_value()}",
            api_key=os.environ.get("GOOGLEGENAI_API_KEY"),
        )
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        llm = LitellmModel(
            model=f"openai/{model.get_name_value()}",
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    return llm
