from typing import Dict
from utils.model import Model, ModelProvider, ModelName


MODELS: Dict[ModelName, Model] = {
    ModelName.DEEPSEEK_R1: Model(
        provider=ModelProvider.OLLAMA, name=ModelName.DEEPSEEK_R1
    ),
    ModelName.LLAMA3_2: Model(provider=ModelProvider.OLLAMA, name=ModelName.LLAMA3_2),
    ModelName.MISTRAL_SMALL_2506: Model(
        provider=ModelProvider.MISTRAL, name=ModelName.MISTRAL_SMALL_2506
    ),
    ModelName.MISTRAL_MEDIUM_2508: Model(
        provider=ModelProvider.MISTRAL, name=ModelName.MISTRAL_MEDIUM_2508
    ),
    ModelName.GPT_4O_MINI: Model(
        provider=ModelProvider.OPENAI, name=ModelName.GPT_4O_MINI
    ),
    ModelName.GPT_4O: Model(provider=ModelProvider.OPENAI, name=ModelName.GPT_4O),
    ModelName.GPT_3_5_TURBO: Model(
        provider=ModelProvider.OPENAI, name=ModelName.GPT_3_5_TURBO
    ),
}


def get_model_by_name(name: ModelName) -> Model:
    if name not in MODELS:
        raise ValueError(f"Model name {name} not recognized.")
    return MODELS[name]


def get_default_model() -> Model:
    return MODELS[ModelName.GPT_4O_MINI]
