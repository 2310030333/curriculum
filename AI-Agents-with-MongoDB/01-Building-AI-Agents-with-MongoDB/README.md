# AI Agents with MongoDB Skill

This repository contains code for an AI Agent that can:
- Answer questions about MongoDB using the MongoDB documentation as a knowledge base
- Summarize content from MongoDB documentation pages

## Project Structure

You can either:
- Run the completed agent in the root directory, or
- Follow the step-by-step implementation in the `lessons` directory

Each lesson builds upon the previous one, providing a gradual learning experience. If working through the lessons, copy the `key_param.py` file to each lesson directory (`lessons/02-*/`, `lessons/03-*/`, etc.) as you progress.

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account with a cluster
- API Keys:
  - VoyageAI API key for embeddings
  - OpenAI API key for the language model

> **Note:** While this demo uses VoyageAI and OpenAI, you can modify the code to work with alternative providers.

## Setup Instructions

1. Configure your API keys in `key_param.py`:
   ```python
   openai_api_key = "your_openai_api_key"
   voyage_api_key = "your_voyage_api_key"
   mongodb_uri = "your_mongodb_uri"
   ```

2. Install the `uv` package manager:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create and initialize a `uv` environment:
   ```bash
   uv init
   ```

4. Install the required dependencies:
   ```bash
   uv add langchain==0.3.24 langchain-openai==0.3.14 langgraph==0.3.31 langgraph-checkpoint-mongodb==0.1.3 pymongo==4.11.3 voyageai==0.3.2
   ```

> **Note:** This project uses the `uv` package manager. If you prefer `pip` or `pipenv`, you'll need to adapt the installation commands.

## Loading the Dataset

Before using the agent, you must load the MongoDB documentation data into your database:

```bash
uv run data.py
```

## Running the Agent

1. In main.py, customize the queries for your agent. Examples:
   ```python
   # Ask a specific question about MongoDB
   execute_graph(app, "1", "What are some best practices for data backups in MongoDB?")
   
   # Test the agent's memory capabilities
   execute_graph(app, "1", "What did I just ask?")
   ```

2. Run the agent:
   ```bash
   uv run main.py
   ```

## Troubleshooting

If you encounter any issues, ensure that:
- Your API keys are correctly set in key_param.py
- Your MongoDB Atlas cluster is accessible from your IP address
- You've loaded the data using data.py before running the agent
