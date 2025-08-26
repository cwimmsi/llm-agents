from typing import Dict
from utils.model import Model, ModelProvider, ModelName


MODELS: Dict[ModelName, Model] = {
    ModelName.PHI4_MINI: Model(provider=ModelProvider.OLLAMA, name=ModelName.PHI4_MINI),
    ModelName.DEEPSEEK_R1: Model(
        provider=ModelProvider.OLLAMA, name=ModelName.DEEPSEEK_R1
    ),
    ModelName.LLAMA3_2: Model(provider=ModelProvider.OLLAMA, name=ModelName.LLAMA3_2),
    ModelName.MISTRAL_SMALL: Model(
        provider=ModelProvider.MISTRALAI, name=ModelName.MISTRAL_SMALL
    ),
    ModelName.MISTRAL_MEDIUM: Model(
        provider=ModelProvider.MISTRALAI, name=ModelName.MISTRAL_MEDIUM
    ),
    ModelName.MISTRAL_LARGE: Model(
        provider=ModelProvider.MISTRALAI, name=ModelName.MISTRAL_LARGE
    ),
    ModelName.GPT_4O_MINI: Model(
        provider=ModelProvider.OPENAI, name=ModelName.GPT_4O_MINI
    ),
    ModelName.GPT_4_1_NANO: Model(
        provider=ModelProvider.OPENAI, name=ModelName.GPT_4_1_NANO
    ),
    ModelName.GPT_5_NANO: Model(
        provider=ModelProvider.OPENAI, name=ModelName.GPT_5_NANO
    ),
    ModelName.GEMINI_2_5_FLASH: Model(
        provider=ModelProvider.GOOGLEGENAI, name=ModelName.GEMINI_2_5_FLASH
    ),
    ModelName.GEMINI_2_5_FLASH_LITE: Model(
        provider=ModelProvider.GOOGLEGENAI, name=ModelName.GEMINI_2_5_FLASH_LITE
    ),
}


def get_model_by_name(name: ModelName) -> Model:
    if name not in MODELS:
        raise ValueError(f"Model name {name} not recognized.")
    return MODELS[name]


def get_default_model() -> Model:
    return MODELS[ModelName.GPT_4O_MINI]
