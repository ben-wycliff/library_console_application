while True:
    print("""
          Choose an option\n
          1. Get all books
          2. Add a book
          3. Delete a book
          4. Edit a book
          """)
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
        break