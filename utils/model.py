from pydantic import BaseModel, Field
from enum import Enum


class ModelName(str, Enum):
    PHI4_MINI = "phi4-mini:3.8b"
    DEEPSEEK_R1 = "deepseek-r1:1.5b"
    LLAMA3_2 = "llama3.2:3b"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"
    MISTRAL_SMALL = "mistral-small-latest"
    MISTRAL_MEDIUM = "mistral-medium-latest"
    MISTRAL_LARGE = "mistral-large-latest"
    GEMINI_2_5_FLASH = "gemini-2.5-flash"
    GEMINI_2_5_FLASH_LITE = "gemini-2.5-flash-lite"


class ModelProvider(str, Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"
    MISTRALAI = "mistralai"
    GOOGLEGENAI = "googlegenai"


class Model(BaseModel):
    provider: ModelProvider = Field(..., description="The provider of the model.")
    name: ModelName = Field(..., description="The name of the model.")

    def get_provider_value(self) -> str:
        return self.provider.value

    def get_name_value(self) -> str:
        return self.name.value
