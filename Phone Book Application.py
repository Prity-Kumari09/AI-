#Create a program that uses dictionaries to build a simple phone book application (add contacts, search by name, delete contacts).
# Phone Book Application

# Initialize an empty dictionary to store contacts
phone_book = {}

def add_contact():
    """
    Add a new contact to the phone book
    """
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    phone_book[name] = phone_number
    print(f"Contact {name} added successfully!")

def search_contact():
    """
    Search for a contact by name
    """
    name = input("Enter the name to search: ")
    if name in phone_book:
        print(f"Phone number of {name} is {phone_book[name]}")
    else:
        print(f"Contact {name} not found!")

def delete_contact():
    """
    Delete a contact from the phone book
    """
    name = input("Enter the name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")

def display_phone_book():
    """
    Display all contacts in the phone book
    """
    print("Phone Book:")
    for name, phone_number in phone_book.items():
        print(f"{name}: {phone_number}")

def main():
    while True:
        print("Phone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Phone Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_phone_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()