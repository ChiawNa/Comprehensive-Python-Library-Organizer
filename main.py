from art import logo
import os

end_of_system = False

books = []

def display():
    print("Book lists: ")
    if not books:  # Check if the books list is empty
        print("The book lists is empty.")
    else:
        for book in books:
            print(f"Name: {book['name']}, \nAuthor: {book['author']}, \nPages: {book['pages']}\n")


def add():
    book_name = str(input("Insert the book name: ")).strip()
    book_author = str(input("Insert the book author: ")).strip()
    book_pages = str(input("Insert the book pages: ")).strip()
    books.append({"name": book_name, "author": book_author, "pages": book_pages})
    print(f"Book '{book_name}' by {book_author} with {book_pages} pages has been added.")


def remove():
    book_name = str(input("Insert the book name to delete: ")).strip()
    for book in books:
        if book['name'] == book_name:
            books.remove(book)
            print(f"Book '{book_name}' removed.")
            return
    print(f"Book '{book_name}' not found.")


def search():
    book_name = input("Insert the book name to search: ").strip()
    for book in books:
        if book['name'].lower() == book_name.lower():
            print(f"Book found: Name: {book['name']}, Author: {book['author']}, Pages: {book['pages']}")
            return
    print(f"Book '{book_name}' not found.")


def save_list():
    base_filename = "receipt"
    counter = 1
    filename = f"{base_filename}.txt"
    
    # Check if the file already exists and modify the filename if it does
    while os.path.exists(filename):
        counter += 1
        filename = f"{base_filename}{counter}.txt"
    
    with open(filename, "w") as file:
        for book in books:
            file.write(f"Name: {book['name']}| Author: {book['author']}| Pages: {book['pages']}\n")
    
    print(f"Book list has been saved successfully as {filename}.")

    # Clear the books list after saving
    books.clear()
    

def load_list():
    filename = input("Enter the filename to load (e.g., receipt.txt): ").strip()
    
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return
    
    global books
    books = []  # Clear the current list
    
    with open(filename, "r") as file:
        print(f"Loading contents from {filename}...")
        for line in file:
            # Print the raw line from the file for user reference
            print(line.strip())
            
            try:
                # Assuming the format in file is: Name|Author|Pages
                name, author, pages = line.strip().split('|')
                books.append({"name": name.strip(), "author": author.strip(), "pages": pages.strip()})
            except ValueError:
                print(f"Line format error in file '{filename}'. Skipping line.")
    
    print(f"Book list successfully loaded from {filename}.")




while not end_of_system: 
    print(logo)
    print("----- Library Management System -----\n")
    print("1. Display Book Lists")
    print("2. Add Books")
    print("3. Remove Books")
    print("4. Search Books")
    print("5. Save Books List")
    print("6. Load Books List")
    print("7. Exit\n")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        display()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        search()
    elif choice == "5":
        save_list()
    elif choice == "6":
        load_list()
    elif choice == "7":
        end_of_system = True
    else:
        print("Invalid input. Please select number from 1-7.")
