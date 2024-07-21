'''Contact Book
Description: An application to store and manage contact information, allowing users to add, delete, and search for contacts.'''

contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added {name} with number {number} to contacts.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")

def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(name, number)
        
        elif choice == '2':
            view_contacts()
        
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":        
    main()
