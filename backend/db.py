from pymongo import MongoClient

def get_db_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["erp_db"]  # Database name
    return db

# Access to the users collection
def get_users_collection():
    db = get_db_connection()
    return db["users"]

# Optional: Access to other collections, such as for documents
def get_documents_collection():
    db = get_db_connection()
    return db["documents"]