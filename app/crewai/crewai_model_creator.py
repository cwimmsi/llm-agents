from crewai import LLM
from playground.data.models import get_default_model
from utils.model import Model, ModelProvider
from utils.logger import setup_logger


def model_creator(model: Model):
    logger = setup_logger()

    temperature = 0.0

    if model.provider == ModelProvider.OLLAMA:
        llm = LLM(
            model=f"ollama/{model.get_name_value()}",
            base_url="http://localhost:11434",
            temperature=temperature,
        )
    elif model.provider == ModelProvider.MISTRALAI:
        llm = LLM(
            model=f"mistral/{model.get_name_value()}",
            temperature=temperature,
        )
    elif model.provider == ModelProvider.OPENAI:
        llm = LLM(
            model=f"openai/{model.get_name_value()}",
            temperature=temperature,
        )
    elif model.provider == ModelProvider.GOOGLEGENAI:
        llm = LLM(
            model=f"gemini/{model.get_name_value()}",
            temperature=temperature,
        )
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        llm = LLM(
            model=f"openai/{model.get_name_value()}",
            temperature=temperature,
        )

    return llm
