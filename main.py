from playground.models import get_model_by_name
from playground.run_n8n import run_n8n_endpoint_prod, run_n8n_endpoint_test
from playground.run_langchain import run_langchain
from playground.run_llamaindex import run_llamaindex
from playground.run_pydanticai import run_pydanticai
from playground.run_openai import run_openai
from playground.run_crewai import run_crewai
from utils.logger import setup_logger
from utils.model import ModelName

logger = setup_logger()


if __name__ == "__main__":
    logger.info("===============")
    logger.info("N8N: Starting ticket processing...")
    # test endpoint
    # run_n8n_endpoint_test(3)
    # production endpoint
    # run_n8n_endpoint_prod(1)
    # run_n8n_endpoint_prod(2)
    # run_n8n_endpoint_prod(3)
    # run_n8n_endpoint_prod(4)

    logger.info("===============")
    logger.info("LANGCHAIN: Starting ticket processing...")
    # run_langchain(1, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_langchain(2, 1, get_model_by_name(ModelName.MISTRAL_SMALL))
    # run_langchain(3, 1, get_model_by_name(ModelName.GEMINI_2_5_FLASH_LITE))
    # run_langchain(4, 1, get_model_by_name(ModelName.DEEPSEEK_R1))

    logger.info("===============")
    logger.info("LLAMAINDEX: Starting ticket processing...")
    # run_llamaindex(1, 1, get_model_by_name(ModelName.GEMINI_2_5_FLASH_LITE))
    # run_llamaindex(2, 1, get_model_by_name(ModelName.MISTRAL_LARGE))
    # run_llamaindex(3, 1, get_model_by_name(ModelName.DEEPSEEK_R1))
    # run_llamaindex(4, 1, get_model_by_name(ModelName.GPT_4O_MINI))

    logger.info("===============")
    logger.info("PYDANTICAI: Starting ticket processing...")
    # run_pydanticai(1, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_pydanticai(2, 1, get_model_by_name(ModelName.MISTRAL_SMALL))
    # run_pydanticai(3, 1, get_model_by_name(ModelName.GEMINI_2_5_FLASH_LITE))
    # run_pydanticai(4, 1, get_model_by_name(ModelName.LLAMA3_2))

    logger.info("===============")
    logger.info("OPENAISDK: Starting ticket processing...")
    # run_openai(1, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_openai(2, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_openai(3, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_openai(4, 1, get_model_by_name(ModelName.GPT_4O_MINI))

    logger.info("===============")
    logger.info("CREWAI: Starting ticket processing...")
    # run_crewai(1, 1, get_model_by_name(ModelName.GPT_4O_MINI))
    # run_crewai(2, 1, get_model_by_name(ModelName.MISTRAL_MEDIUM))
    # run_crewai(3, 1, get_model_by_name(ModelName.GEMINI_2_5_FLASH))
    # run_crewai(4, 1, get_model_by_name(ModelName.PHI4_MINI))
