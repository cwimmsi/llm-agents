import argparse
from typing import Callable
from playground.run_crewai import run_crewai
from playground.run_langchain import run_langchain
from playground.run_llamaindex import run_llamaindex
from playground.run_n8n import run_n8n, run_n8n_test
from playground.run_openai import run_openai
from playground.run_pydanticai import run_pydanticai
from playground.data.models import get_model_by_name
from playground.data.tickets import TICKET_DATASET
from utils.logger import setup_logger
from utils.model import ModelName

logger = setup_logger()


def start_experiment_for(
    agent_run_func: Callable, model_name: ModelName, ticket_id: int = None
):
    logger.info(
        f"Starting experiment with agent run function '{agent_run_func.__name__}' and model '{model_name}'"
    )
    if ticket_id is not None:
        agent_run_func(ticket_id, get_model_by_name(model_name))
    else:
        for i in range(1, len(TICKET_DATASET) + 1):
            agent_run_func(i, get_model_by_name(model_name))

    logger.info("Experiment completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run ticket processing with different agents and models."
    )
    parser.add_argument(
        "--agent", type=str, required=True, help="The name of the agent to use."
    )
    parser.add_argument(
        "--model", type=str, required=True, help="The model name to use."
    )
    parser.add_argument(
        "--ticket", type=int, required=False, help="The ticket ID to process."
    )
    args = parser.parse_args()

    # Map agent names to actual functions
    agent_function_mapping = {
        "crewai": run_crewai,
        "langchain": run_langchain,
        "llamaindex": run_llamaindex,
        "n8n": run_n8n,
        "n8n-test": run_n8n_test,
        "openai": run_openai,
        "pydanticai": run_pydanticai,
    }

    # Get the agent function from the mapping
    agent_function = agent_function_mapping.get(args.agent)
    if agent_function is None:
        logger.error(f"Invalid agent function: {args.agent}")
        exit(1)

    model_name_str = args.model
    try:
        # Parse model name to ModelName object
        model_name = ModelName(model_name_str)
    except ValueError:
        logger.error(f"Invalid model name: {model_name_str}")
        exit(1)

    ticket_id = args.ticket if args.ticket else None

    start_experiment_for(
        agent_run_func=agent_function,
        model_name=model_name,
        ticket_id=ticket_id,
    )
