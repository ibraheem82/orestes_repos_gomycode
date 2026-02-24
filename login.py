def basic_login():
    valid_credentials = {
        "admin": "password123",
        "user" : "userpass",
        "john" : "john123"
    }
    print("=== Login SYSTEM ===")

    username = input("Enter username: ")
    password = input("Enter password: ")