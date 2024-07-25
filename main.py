# from art import logo
# import os

# end_of_system = False
# books = []


# def display():
#     print("Book lists: ")
#     if not books:  # Check if the books list is empty
#         print("The book lists is empty.")
#     else:
#         for book in books:
#             print(f"Name: {book['name']}, \nAuthor: {book['author']}, \nPages: {book['pages']}\n")


# def add():
#     book_name = str(input("Insert the book name: ")).strip()
#     book_author = str(input("Insert the book author: ")).strip()
#     book_pages = str(input("Insert the book pages: ")).strip()
#     books.append({"name": book_name, "author": book_author, "pages": book_pages})
#     print(f"Book '{book_name}' by {book_author} with {book_pages} pages has been added.")


# def remove():
#     book_name = str(input("Insert the book name to delete: ")).strip()
#     for book in books:
#         if book['name'] == book_name:
#             books.remove(book)
#             print(f"Book '{book_name}' removed.")
#             return
#     print(f"Book '{book_name}' not found.")


# def search():
#     book_name = input("Insert the book name to search: ").strip()
#     for book in books:
#         if book['name'].lower() == book_name.lower():
#             print(f"Book found: Name: {book['name']}, Author: {book['author']}, Pages: {book['pages']}")
#             return
#     print(f"Book '{book_name}' not found.")


# def save_list():
#     base_filename = "receipt"
#     counter = 1
#     filename = f"{base_filename}.txt"
    
#     # Check if the file already exists and modify the filename if it does
#     while os.path.exists(filename):
#         counter += 1
#         filename = f"{base_filename}{counter}.txt"
    
#     with open(filename, "w") as file:
#         for book in books:
#             file.write(f"Name: {book['name']}| Author: {book['author']}| Pages: {book['pages']}\n")
    
#     print(f"Book list has been saved successfully as {filename}.")

#     # Clear the books list after saving
#     books.clear()
    

# def load_list():
#     filename = input("Enter the filename to load (e.g., receipt.txt): ").strip()
    
#     if not os.path.exists(filename):
#         print(f"File '{filename}' does not exist.")
#         return
    
#     global books
#     books = []  # Clear the current list
    
#     with open(filename, "r") as file:
#         print(f"Loading contents from {filename}...")
#         for line in file:
#             # Print the raw line from the file for user reference
#             print(line.strip())
            
#             try:
#                 # Assuming the format in file is: Name: book_name| Author: book_author| Pages: book_pages
#                 name, author, pages = line.strip().split('|')
#                 book_name = name.split(':', 1)[1].strip()
#                 book_author = author.split(':', 1)[1].strip()
#                 book_pages = pages.split(':', 1)[1].strip()
#                 books.append({"name": book_name, "author": book_author, "pages": book_pages})
#             except ValueError:
#                 print(f"Line format error in file '{filename}'. Skipping line.")
    
#     print(f"Book list successfully loaded from {filename}.")
#     display()  # Display the loaded book list


# while not end_of_system: 
#     print(logo)
#     print("----- Library Management System -----\n")
#     print("1. Display Book Lists")
#     print("2. Add Books")
#     print("3. Remove Books")
#     print("4. Search Books")
#     print("5. Save Books List")
#     print("6. Load Books List")
#     print("7. Exit\n")

#     choice = input("Enter your choice (1-7): ")

#     if choice == "1":
#         display()
#     elif choice == "2":
#         add()
#     elif choice == "3":
#         remove()
#     elif choice == "4":
#         search()
#     elif choice == "5":
#         save_list()
#     elif choice == "6":
#         load_list()
#     elif choice == "7":
#         end_of_system = True
#     else:
#         print("Invalid input. Please select number from 1-7.")



from art import logo
import os

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.end_of_system = False

    def display(self):
        print("Book lists: ")
        if not self.books:
            print("The book list is empty.")
        else:
            for book in self.books:
                print(f"Name: {book['name']}\nAuthor: {book['author']}\nPages: {book['pages']}\n")

    def add(self):
        book_name = input("Insert the book name: ").strip()
        book_author = input("Insert the book author: ").strip()
        book_pages = input("Insert the book pages: ").strip()
        self.books.append({"name": book_name, "author": book_author, "pages": book_pages})
        print(f"Book '{book_name}' by {book_author} with {book_pages} pages has been added.")

    def remove(self):
        book_name = input("Insert the book name to delete: ").strip()
        for book in self.books:
            if book['name'].lower() == book_name.lower():
                self.books.remove(book)
                print(f"Book '{book_name}' removed.")
                return
        print(f"Book '{book_name}' not found.")

    def search(self):
        book_name = input("Insert the book name to search: ").strip()
        for book in self.books:
            if book['name'].lower() == book_name.lower():
                print(f"Book found: Name: {book['name']}, Author: {book['author']}, Pages: {book['pages']}")
                return
        print(f"Book '{book_name}' not found.")

    def save_list(self):
        filename = input("Enter the filename to save as: ").strip()
        if not filename:
            print("Invalid filename.")
            return

        with open(filename, "w") as file:
            for book in self.books:
                file.write(f"Name: {book['name']}| Author: {book['author']}| Pages: {book['pages']}\n")
        print(f"Book list has been saved successfully as {filename}.")
        self.books.clear()

    def load_list(self):
        filename = input("Enter the filename to load: ").strip()
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        
        with open(filename, "r") as file:
            print(f"Loading contents from {filename}...")
            for line in file:
                print(line.strip())
                try:
                    name, author, pages = line.strip().split('|')
                    book_name = name.split(':', 1)[1].strip()
                    book_author = author.split(':', 1)[1].strip()
                    book_pages = pages.split(':', 1)[1].strip()
                    self.books.append({"name": book_name, "author": book_author, "pages": book_pages})
                except ValueError:
                    print(f"Line format error in file '{filename}'. Skipping line.")
        
        print(f"Book list successfully loaded from {filename}.")
        self.display()

    def run(self):
        while not self.end_of_system:
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
                self.display()
            elif choice == "2":
                self.add()
            elif choice == "3":
                self.remove()
            elif choice == "4":
                self.search()
            elif choice == "5":
                self.save_list()
            elif choice == "6":
                self.load_list()
            elif choice == "7":
                self.end_of_system = True
            else:
                print("Invalid input. Please select a number from 1-7.")

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
