import pymongo

# Connect to MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as needed
db = mongo_client["erp_db"]  # Replace with your database name
users_collection = db["users"]  # Replace with your collection name

# Function to create a new user
def create_user(username, password, role, name):
    user_data = {
        "username": username,
        "password": password,  # Store the plain text password
        "role": role,
        "name": name  # Store the actual name of the user
    }
    users_collection.insert_one(user_data)  # Save to MongoDB
    print(f"User {username} created successfully!")

# Function to verify user
def verify_user(username, password):
    user = users_collection.find_one({"username": username})  # Fetch user from the database
    if user and user['password'] == password:  # Directly compare the password
        print("Login successful!")
    else:
        print("Login failed!")

# Create a new user
create_user("faizan", "faizan123", "admin", "Faizan")  # Adjust these values as needed

# Verify the created user
verify_user("faizan", "faizan123")  # Adjust these values as needed
