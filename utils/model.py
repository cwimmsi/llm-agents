from pydantic import BaseModel, Field
from enum import Enum


class ModelName(str, Enum):
    PHI4_MINI = "phi4-mini:3.8b"  # ollama, open-source
    DEEPSEEK_R1 = "deepseek-r1:1.5b"  # ollama, open-source
    LLAMA3_2 = "llama3.2:3b"  # ollama, open-source
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    GPT_5_MINI = "gpt-5-mini"
    MISTRAL_SMALL_2506 = "mistral-small-2506"  # available open-source too
    MISTRAL_MEDIUM_2508 = "mistral-medium-2508"
    MAGISTRAL_SMALL_2507 = "magistral-small-2507"  # available open-source too
    MAGISTRAL_MEDIUM_2507 = "magistral-medium-2507"


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
