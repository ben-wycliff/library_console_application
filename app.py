from pymongo import MongoClient



URI = "mongodb://127.0.0.1:27017/"
client = MongoClient(URI)
print("\n===================== connection successful =====================\n")

def print_options():
    print("""
          Choose Option:\n
          1. Get all books
          2. Add a book
          3. Delete a book
          """)
    
def print_add_book():
    print("Enter title:\n")
    title = str(input())
    print("Enter author: \n")
    author = str(input())
    return title, author

def print_delete_book():
    print("Enter book title:\n")
    title = str(input())
    return title

while True:
    print_options()
    response = int(input())
    
    if response == 1:
        books = client.library.books.find({})
        print("Books:\n")
        for i, book in enumerate(books):
            print(str(i+1)+"\t"+book["title"])
        
    elif response == 2:
        title, author = print_add_book()
        client.library.books.insert_one({"title": title, "author": author})
        print("Book titled " + title + " has been registered successfully.")
        
    elif response == 3:
        title = print_delete_book()
        client.library.books.delete_one({"title": title})
        print("Book titled "+ title + " has been deleted.")
        
    else:
        print("Exiting library")
        client.close()
        break