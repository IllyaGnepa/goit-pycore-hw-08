import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email})"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Add a new contact to the address book
        self.contacts.append(contact)

    def remove_contact(self, name):
        # Remove a contact by name from the address book
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def find_contact(self, name):
        # Find a contact by name in the address book
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def __repr__(self):
        return f"AddressBook(contacts={self.contacts})"

def save_data(book, filename="addressbook.pkl"):
    # Save the address book to a file using pickle
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
    except IOError as e:
        print(f"Error saving data: {e}")

def load_data(filename="addressbook.pkl"):
    # Load the address book from a file using pickle. If file does not exist, return a new AddressBook
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No previous data found, starting with a new address book.")
        return AddressBook()
    except IOError as e:
        print(f"Error loading data: {e}")
        return AddressBook()
    except pickle.PickleError as e:
        print(f"Error loading data: {e}")
        return AddressBook()

def main():
    # Main function to run the address book application
    book = load_data()

    while True:
        print("\nAddress Book")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Find Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new contact
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            book.add_contact(contact)
            print(f"Contact {name} added.")

        elif choice == "2":
            # Remove an existing contact
            name = input("Enter name of contact to remove: ")
            if book.find_contact(name):
                book.remove_contact(name)
                print(f"Contact {name} removed.")
            else:
                print(f"Contact {name} not found.")

        elif choice == "3":
            # Find and display a contact
            name = input("Enter name of contact to find: ")
            contact = book.find_contact(name)
            if contact:
                print(f"Found: {contact}")
            else:
                print("Contact not found.")

        elif choice == "4":
            # Save data and exit
            save_data(book)
            print("Address book saved. Exiting.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
