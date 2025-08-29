from pydantic import BaseModel, Field
from enum import Enum


class ModelName(str, Enum):
    DEEPSEEK_R1 = "deepseek-r1:1.5b"  # via ollama, open-source, 1,5B parameters
    LLAMA3_2 = "llama3.2:3b"  # via ollama, open-source, 3B parameters
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    MISTRAL_SMALL_2506 = "mistral-small-2506"
    MISTRAL_MEDIUM_2508 = "mistral-medium-2508"


class ModelProvider(str, Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"
    MISTRAL = "mistral"


class Model(BaseModel):
    provider: ModelProvider = Field(..., description="The provider of the model.")
    name: ModelName = Field(..., description="The name of the model.")

    def get_provider_value(self) -> str:
        return self.provider.value

    def get_name_value(self) -> str:
        return self.name.value
