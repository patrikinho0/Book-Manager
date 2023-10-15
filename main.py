import os
from time import sleep
from utils import *

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the Book Manager")
sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')

print("Available options: ")
print("1 - add new book")
print("2 - display all books")
print("3 - display books lower than price input")
print("4 - display books higher than price input")
print("5 - display books where author is like input")
print("6 - display books lower than year input")
print("7 - display books higher than year input")

choice = int(input("Enter your choice: "))

if choice == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    isbn = int(input("Enter ISBN: "))
    name = input("Enter name: ")
    description = input("Enter description: ")
    publish_year = int(input("Enter publish year: "))
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    add_new_book(isbn, name, description, publish_year, author, price)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Adding new book...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Book successfully added!")

elif choice == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Displaying books...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    display_all_books("books.json")

elif choice == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    price_input = float(input("Enter the price input: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    display_lower_price("books.json", price_input)

elif choice == 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    price_input = float(input("Enter the price input: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    display_higher_price("books.json", price_input)

elif choice == 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    author_input = input("Enter the author input: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    display_author_books("books.json", author_input)

elif choice == 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    year_input = int(input("Enter the year input: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching...")
    os.system('cls' if os.name == 'nt' else 'clear')
    display_lower_year("books.json", year_input)

elif choice == 7:
    os.system('cls' if os.name == 'nt' else 'clear')
    year_input = int(input("Enter the year input: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching...")
    os.system('cls' if os.name == 'nt' else 'clear')
    display_higher_year("books.json", year_input)

else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ERROR! Invalid choice!")