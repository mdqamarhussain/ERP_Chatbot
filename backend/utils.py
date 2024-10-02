import hashlib
def format_response(data):

    # Utility function to format response data
    return {"status": "success", "data": data}



# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()