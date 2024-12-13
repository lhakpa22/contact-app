from hash_table import HashTable, Contact


def display_menu():
    print("\nContact Management App")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Find Contact")
    print("5. List Contacts")
    print("6. Exit")


if __name__ == "__main__":
    hash_table = HashTable(size=10, method="open_addressing")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")
            hash_table.add_contact(Contact(name, phone, address))
        elif choice == "2":
            name = input("Enter name to update: ")
            phone = input("Enter new phone: ")
            address = input("Enter new address: ")
            hash_table.update_contact(name, Contact(name, phone, address))
        elif choice == "3":
            name = input("Enter name to delete: ")
            hash_table.delete_contact(name)
        elif choice == "4":
            name = input("Enter name to find: ")
            contact = hash_table.find_contact(name)
            print(contact if contact else "Contact not found.")
        elif choice == "5":
            contacts = hash_table.list_contacts()
            for contact in contacts:
                print(contact)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
