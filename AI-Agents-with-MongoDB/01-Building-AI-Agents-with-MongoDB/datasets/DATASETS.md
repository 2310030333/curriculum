# Datasets for Building AI Agents with MongoDB

To restore the sample dataset including the `chunked_docs` and `full_docs` collections from this project, you can use the `ai_agents.gz` file in this directory. Restoring this dataset can be done instead of executing the `load_data.py` if you want to skip the data loading step.

- `full_docs`: Contains the complete documents sourced from the Hugging Face `mongodb-docs` sample dataset, which can be found [here](https://huggingface.co/datasets/MongoDB/mongodb-docs)
- `chunked_docs`: Contains the vector embeddings (generated using [Voyage AI](https://github.com/voyage-ai/voyageai-python)) from the parsed PDF file for "The Little MongoDB Book" by Karl Seguin located [here](https://www.openmymind.net/mongodb.pdf)

## Instructions to Restore the Dataset

1. Download the `ai_agents.gz` file from the project repository.
2. Use the following command to restore the dataset:

```bash
mongorestore --archive="ai_agents.gz" --gzip --nsFrom="ai_agents_test.*" --nsTo="ai_agents.*" <connection_string> --drop
```

This should restore `20` documents in the `full_docs` collection and `107` documents in the `chunked_docs` collection. You can verify the restoration by connecting to your MongoDB instance and checking the collections.

```bash
mongosh <connection_string> --eval "use ai_agents" --eval "db.full_docs.countDocuments()" --shell
```