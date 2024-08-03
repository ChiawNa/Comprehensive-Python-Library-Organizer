from art import logo1, logo2, logo3, logo4, logo5
import os


class LibraryManagementSystem:
    def __init__(self):
        self.books = [
            {"logo": logo1, "name": "1984", "author": "George Orwell", "pages": "328"},
            {"logo": logo2, "name": "To Kill a Mockingbird", "author": "Harper Lee", "pages": "281"},
            {"logo": logo3,"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": "180"},
            {"logo": logo4,"name": "Moby-Dick", "author": "Herman Melville", "pages": "635"}, 
            {"logo": logo5,"name": "The Hobbit", "author": "J.R.R. Tolkien", "pages": "310"}                        
        ]
        self.borrowed_books = []
        self.end_of_system = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        system.clear()
        print("Book lists: ")
        if not self.books:
            print("The book list is empty.")
        else:
            for book in self.books:
                if book.get("logo"):
                    print(book["logo"])
                    print(f"Name: {book['name']}\nAuthor: {book['author']}\nPages: {book['pages']}\n\n")

        # print("Borrowed Books: ")
        # if not self.borrowed_books:
        #     print("No books borrowed.")
        # else:
            for book in self.borrowed_books:
                if book.get("logo"):
                    print(book["logo"])
                    print(f"Name: {book['name']}\nAuthor: {book['author']}\nPages: {book['pages']}\n\n")


    def borrow(self):
        system.clear()
        system.display()
        book_name = input("Insert the book name to borrow: ").strip()
        for book in self.books:
            if book['name'].lower() == book_name.lower():
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Book '{book_name}' borrowed.")
                return
        print(f"Book '{book_name}' not found or already borrowed.")


    def return_back(self):
        self.clear()
        book_name = input("Insert the book name to return: ").strip()
        for book in self.borrowed_books:
            if book['name'].lower() == book_name.lower():
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Book '{book_name}' returned.")
                return
        print(f"Book '{book_name}' not found in borrowed books.")


    def search(self):
        system.clear()
        book_name = input("Insert the book name to search: ").strip()
        for book in self.books + self.borrowed_books:
            if book['name'].lower() == book_name.lower():
                print(f"Book found: Name: {book['name']}, Author: {book['author']}, Pages: {book['pages']}")
                return
        print(f"Book '{book_name}' not found.")


    def save_list(self):
        system.clear()
        filename = input("Enter the filename to save as: ").strip()
        if not filename:
            print("Invalid filename.")
            return

        with open(filename, "w") as file:
            for book in self.books:
                file.write(f"Available: Name: {book['name']}| Author: {book['author']}| Pages: {book['pages']}\n")
            for book in self.borrowed_books:
                file.write(f"Borrowed: Name: {book['name']}| Author: {book['author']}| Pages: {book['pages']}\n")
        print(f"Book list has been saved successfully as {filename}.")
        self.books.clear()
        self.borrowed_books.clear()


    def load_list(self):
        system.clear()
        filename = input("Enter the filename to load: ").strip()
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        
        with open(filename, "r") as file:
            print(f"Loading contents from {filename}...")
            for line in file:
                print(line.strip())
                try:
                    status, rest = line.strip().split(': ', 1)
                    name, author, pages = line.strip().split('|')
                    book_name = name.split(':', 1)[1].strip()
                    book_author = author.split(':', 1)[1].strip()
                    book_pages = pages.split(':', 1)[1].strip()
                    book = {"name": book_name, "author": book_author, "pages": book_pages}

                    if status == "Available":
                        self.books.append(book)
                    elif status == "Borrowed":
                        self.borrowed_books.append(book)
                except ValueError:
                    print(f"Line format error in file '{filename}'. Skipping line.")
        
        print(f"Book list successfully loaded from {filename}.")
        self.display()


    def run(self):
        while not self.end_of_system:
            print("----- Library Management System -----\n")
            print("1. Display Book Lists")
            print("2. Borrow Books")
            print("3. Return Books")            
            print("4. Search Books")
            print("5. Save Books List")
            print("6. Load Books List")
            print("7. Exit\n")

            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                self.display()
            elif choice == "2":
                self.borrow()
            elif choice == "3":
                self.return_back()
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
                input("Press Enter to continue...\n")
                print("\n")


if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
