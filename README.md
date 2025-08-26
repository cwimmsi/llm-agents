# LLM-Agents Project

## Project structure

├── app/                # Application code prototypes
  ├── app-crewai/
  ├── app-langgraph/
  └── app-n8n/
├── playground/         # Experimental code
  └── tickets/
├── prompts/            # Centralized prompts
├── tests/              # Unit tests and e2e tests
├── utils/              # Shared objects
├── .env                # Environment variables
├── docker-compose.yml  # Docker container set up
├── pyproject.toml      # Project dependencies and metadata
└── uv.lock             # Locked dependencies


## Virtual environment
Activate venv and set Python interpreter

```uv venv```
```.\.venv\Scripts\activate```

## UV sync
Sync dependencies with environment

```uv sync --link-mode=copy```

To add additional packages use

```uv add %package% --link-mode=copy```