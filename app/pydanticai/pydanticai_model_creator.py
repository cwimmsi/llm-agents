import os
from dotenv import load_dotenv
from pydantic_ai.models import ModelSettings
from pydantic_ai.models.mistral import MistralModel
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.mistral import MistralProvider
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.providers.ollama import OllamaProvider
from playground.models import get_default_model
from utils.model import Model, ModelProvider
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger()


def model_creator(model: Model):
    common_model_settings = ModelSettings(temperature=0.2)

    if model.provider == ModelProvider.OLLAMA:
        # there is no built in Ollama model, but it can be used via OpenAIModel implementation
        llm = OpenAIModel(
            provider=OllamaProvider(base_url="http://localhost:11434/v1"),
            model_name=model.get_name_value(),
            settings=common_model_settings,
        )
    elif model.provider == ModelProvider.MISTRALAI:
        llm = MistralModel(
            provider=MistralProvider(api_key=os.environ.get("MISTRALAI_API_KEY")),
            model_name=model.get_name_value(),
            settings=common_model_settings,
        )
    elif model.provider == ModelProvider.OPENAI:
        llm = OpenAIModel(
            provider=OpenAIProvider(api_key=os.environ.get("OPENAI_API_KEY")),
            model_name=model.get_name_value(),
            settings=common_model_settings,
        )
    elif model.provider == ModelProvider.GOOGLEGENAI:
        llm = GoogleModel(
            provider=GoogleProvider(api_key=os.environ.get("GOOGLEGENAI_API_KEY")),
            model_name=model.get_name_value(),
            settings=common_model_settings,
        )
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        llm = OpenAIModel(
            provider=OpenAIProvider(api_key=os.environ.get("OPENAI_API_KEY")),
            model_name=model.get_name_value(),
            settings=common_model_settings,
        )

    return llm
