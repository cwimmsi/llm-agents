# LLM-Agents Project

## Project structure

```
├── app/                  # Folder containing the prototyp for each framework
   ├── crewai/            # Contains *_agent.py and *_model_creator.py
   ├── langchain/         # Contains *_agent.py and *_model_creator.py
   ├── llamaindex/        # Contains *_agent.py and *_model_creator.py
   ├── n8n/               # Contains n8n data (workflow, data)
   ├── openai/            # Contains *_agent.py and *_model_creator.py
   └── pydanticai/        # Contains *_agent.py and *_model_creator.py
├── logs/                 # Output logs of the experiments
├── playground/           # Experimental code
   ├── data/              # Datasets for the experiments
      ├── expected_classifications.py
      ├── models.py
      └── tickets.py
   ├── evaluate_classification.py   # Evaluates the result
   ├── run_crewai.py      # Executes the prototyp for CrewAI
   ├── run_langchain.py   # Executes the prototyp for LangChain
   ├── run_llamaindex.py  # Executes the prototyp for LlamaIndex
   ├── run_n8n.py         # Executes the prototyp for n8n
   ├── run_openai.py      # Executes the prototyp for OpenAI Agents SDK
   └── run_pydanticai.py  # Executes the prototyp for PydanticAI
├── prompts/              # Centralized prompts (system, user, ...)
├── utils/                # Shared objects for the prototyps
   ├── logger.py          # Global logger object
   ├── model.py           # Pydantic model: Model (for easy switching
                            between models in the *_model_creator.py files)
   └── ticket.py          # Pydantic model: Ticket, TicketClassification
├── .env                  # Environment variables
├── docker-compose.yml    # Docker container set up (n8n, Ollama)
├── pyproject.toml        # Project dependencies and metadata
├── README.md             # Project documentation
└── uv.lock               # Locked dependencies
```

## Virtual environment
Activate venv and set Python interpreter

```
uv venv
.\.venv\Scripts\activate
```

## UV sync
Sync dependencies with environment

```
uv sync --link-mode=copy
```

To add or remove additional packages use

```
uv add {package-name} --link-mode=copy
uv remove {package-name} --link-mode=copy
```

## Environment variables

Set up the following environment variables in your `.env` file

```python
# n8n workflow trigger url
N8N_WEBHOOK_URL_TEST=url_to_test_webhook
N8N_WEBHOOK_URL_PROD=url_to_prod_webhook

# model api keys
OPENAI_API_KEY=your_openai_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

## Spin up Docker container

For the use of n8n and Ollama lokal instance, you need the Docker engine running on your environment. On Windows you can use Docker Desktop.

Create and run containers detached: 
```
docker-compose up -d
```

Stop containers: 
```
docker-compose stop
```

Start containers: 
```
docker-compose start
```

Remove containers (peristent data will be kept): 
```
docker-compose down
```

## Execute experiment

You can run any experiment with `main.py`. Use the command line of your terminal and run via uv package manager and specify arguments for agent and model.

Example:
```
uv .\main.py --agent pydanticai --model gpt-4o-mini
```

### Agents

- crewai
- langchain
- llamaindex
- n8n
- openai
- pydanticai

### Models

Current supported models in the code (lookup `model.py`):

- gpt-4o-mini
- gpt-4o
- gpt-3.5-turbo
- mistral-small-latest
- mistral-medium-latest
- llama3.2:3b (via Ollama)
- deepseek-r1:1.5b (via Ollama)

### Output logs of the experiment
Logs will be written to the folder:

 `logs/{agent}_{model}/run_{agent}_datetime.log`