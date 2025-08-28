import os
from dotenv import load_dotenv
from langchain_ollama.chat_models import ChatOllama
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from playground.data.models import get_default_model
from utils.model import Model, ModelProvider
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger()


def model_creator(model: Model):
    temperature = 0.0

    if model.provider == ModelProvider.OLLAMA:
        llm = ChatOllama(
            model=model.get_name_value(),
            temperature=temperature,
        )
    elif model.provider == ModelProvider.MISTRALAI:
        llm = ChatMistralAI(
            api_key=os.environ.get("MISTRALAI_API_KEY"),
            model=model.get_name_value(),
            temperature=temperature,
        )
    elif model.provider == ModelProvider.OPENAI:
        llm = ChatOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=temperature,
        )
    elif model.provider == ModelProvider.GOOGLEGENAI:
        llm = ChatGoogleGenerativeAI(
            api_key=os.environ.get("GOOGLEGENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=temperature,
        )
    else:
        logger.warning(f"Unsupported model provider: {model.provider}")
        model = get_default_model()
        logger.warning(
            f"Switch to default model: {model.get_provider_value()} {model.get_name_value()}"
        )
        llm = ChatOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model=model.get_name_value(),
            temperature=temperature,
        )

    return llm
