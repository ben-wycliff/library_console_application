from pymongo import MongoClient


def connect_to_database():
    """This function connects to the mongoDB running instance"""
    URI = "mongodb://127.0.0.1:27017/"
    client = MongoClient(URI)
    print("=================== Connection successful ===================\n")

def print_options():
    print("""
          Choose Option:\n
          1. Get all books
          2. Add a book
          3. Delete a book
          4. Edit a book
          """)

while True:
    connect_to_database()
    print_options()
    response = int(input())
    if response == 1:
        print("Getting all books")
    elif response == 2:
        print("Adding a book")
    elif response == 3:
        print("Deleting a book")
    elif response == 4:
        print("Editing a book")
    else:
        print("Exiting library")
        client.close()
        break