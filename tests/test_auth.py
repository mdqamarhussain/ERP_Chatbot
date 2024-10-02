# Example of a simple test for the auth functions (could use pytest or unittest)

def test_hash_password():
    from backend.utils import hash_password
    password = "test123"
    hashed_password = hash_password(password)
    assert hashed_password != password