import key_param
from pymongo import MongoClient
from langchain_openai import ChatOpenAI

def init_mongodb():
    """
    Initialize MongoDB client and collections.

    Returns:
        tuple: MongoDB client, vector search collection, full documents collection.
    """
    mongodb_client = MongoClient(key_param.mongodb_uri)
    
    DB_NAME = "ai_agents"
    
    vs_collection = mongodb_client[DB_NAME]["chunked_docs"]
    
    full_collection = mongodb_client[DB_NAME]["full_docs"]
    
    return mongodb_client, vs_collection, full_collection

def main():
    """
    Main function to initialize and execute the graph.
    """
    # Initialize MongoDB connections
    mongodb_client, vs_collection, full_collection = init_mongodb()
    
    # Initialize the ChatOpenAI model with API key
    llm = ChatOpenAI(openai_api_key=key_param.openai_api_key, temperature=0, model="gpt-4o")
    
    

# Execute main function when script is run directly
main()