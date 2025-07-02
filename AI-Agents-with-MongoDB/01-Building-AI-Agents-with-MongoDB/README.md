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
- [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas/register) with a cluster, or [self-managed](https://www.mongodb.com/docs/atlas/cli/current/atlas-cli-deploy-local/) Atlas cluster
- API Keys:
  - [VoyageAI API key](https://docs.voyageai.com/docs/api-key-and-installation) for embeddings
  - [OpenAI API key](https://platform.openai.com/account/api-keys) for the language model

> [!NOTE]
> While this demo uses VoyageAI and OpenAI, you can modify the code to work with alternative providers.

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

> [!NOTE]
> This project uses the [`uv`](https://docs.astral.sh/uv/) package manager. If you prefer `pip` or `pipenv`, you'll need to adapt the installation commands.

## Loading the Dataset

Before using the agent, you must load the MongoDB documentation data into your database:

```bash
uv run data.py
```

This script loads two Hugging Face datasets, [`mongodb-docs`](https://huggingface.co/datasets/MongoDB/mongodb-docs) (full docs) and [`mongodb-docs-embedded`](https://huggingface.co/datasets/MongoDB/mongodb-docs-embedded) (chunked docs), into your MongoDB instance. Full documents go into `full_docs`; chunked docs are embedded via VoyageAI ([`voyage-3-lite`](https://blog.voyageai.com/2024/09/18/voyage-3/)) and saved to `chunked_docs`. Finally, it creates a [`vector_index`](https://github.com/mongodb-university/curriculum/blob/main/AI-Agents-with-MongoDB/01-Building-AI-Agents-with-MongoDB/data.py#L41-L54) on the `embedding` field for semantic search. See [Attribution](#attribution) for more information.

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

- Your API keys are correctly set in `key_param.py`
- Your MongoDB Atlas cluster is accessible from your IP address
- You've loaded the data using `data.py` before running the agent

## Attribution

### Datasets

- **MongoDB/mongodb-docs** by MongoDB, Inc.  
  License: CC BY 3.0  
  <https://huggingface.co/datasets/MongoDB/mongodb-docs>  
- **MongoDB/mongodb-docs-embedded** by MongoDB, Inc.  
  License: CC BY 3.0  
  <https://huggingface.co/datasets/MongoDB/mongodb-docs-embedded>  

### Models & APIs

- **VoyageAI** (`voyage-3-lite` embeddings)  
  <https://voyageai.com/>  
- **OpenAI** (GPT-4o via langchain-openai)  
  <https://openai.com>
- **MongoDB Atlas** (for database hosting)  
  <https://www.mongodb.com/cloud/atlas>
