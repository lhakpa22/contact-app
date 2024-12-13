class HashTable:
    def __init__(self, size=100, method="separate_chaining"):
        self.size = size
        self.method = method  # "separate_chaining" or "open_addressing"
        self.table = [None] * self.size  # Initialize the hash table with None
        self.deleted = object()  # A unique marker for deleted entries
        self.count = 0  # Number of elements in the table

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def _probe(self, index):
        original_index = index
        while self.table[index] is not None and self.table[index] is not self.deleted:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        return index

    def _resize(self):
        old_table = self.table
        self.size *= 2  # Double the table size
        self.table = [None] * self.size
        self.count = 0  # Reset count

        for entry in old_table:
            if entry is not None and entry is not self.deleted:
                self.add_contact(entry)  # Rehash existing entries

    def add_contact(self, contact):
        if self.method == "open_addressing":
            # Resize if load factor exceeds 0.7
            if self.count / self.size > 0.7:
                self._resize()

        index = self._hash(contact.name)
        if self.method == "separate_chaining":
            if self.table[index] is None:
                self.table[index] = []
            # Avoid duplicates
            for existing_contact in self.table[index]:
                if existing_contact.name == contact.name:
                    print(f"Contact with name {contact.name} already exists.")
                    return
            self.table[index].append(contact)
        elif self.method == "open_addressing":
            index = self._probe(index)
            self.table[index] = contact
            self.count += 1

    def delete_contact(self, name):
        index = self._hash(name)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index].name == name:
                self.table[index] = self.deleted
                self.count -= 1
                print(f"Contact with name {name} deleted.")
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"Contact with name {name} not found.")

    def list_contacts(self):
        all_contacts = []
        for contact in self.table:
            if contact is not None and contact is not self.deleted:
                all_contacts.append(contact)
        return all_contacts

    def find_contact(self, name):
        """Find and return a contact by name."""
        index = self._hash(name)
        if self.method == "separate_chaining":
            if self.table[index] is not None:
                for contact in self.table[index]:
                    if contact.name == name:
                        return contact
        elif self.method == "open_addressing":
            original_index = index
            while self.table[index] is not None:
                if self.table[index] != self.deleted and self.table[index].name == name:
                    return self.table[index]
                index = (index + 1) % self.size
                if index == original_index:
                    break
        print(f"Contact with name {name} not found.")
        return None

    def update_contact(self, name, new_contact):
        """Update an existing contact by name."""
        index = self._hash(name)
        if self.method == "separate_chaining":
            if self.table[index] is not None:
                for i, contact in enumerate(self.table[index]):
                    if contact.name == name:
                        self.table[index][i] = new_contact
                        print(f"Contact with name {name} updated.")
                        return
        elif self.method == "open_addressing":
            original_index = index
            while self.table[index] is not None:
                if self.table[index] != self.deleted and self.table[index].name == name:
                    self.table[index] = new_contact
                    print(f"Contact with name {name} updated.")
                    return
                index = (index + 1) % self.size
                if index == original_index:
                    break
        print(f"Contact with name {name} not found.")


# Create a contact class (if not already defined)
class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.address}"


# Initialize the hash table
hash_table = HashTable(size=10, method="separate_chaining")

# Add contacts
hash_table.add_contact(Contact("John Doe", "555-1234", "123 Elm St"))
hash_table.add_contact(Contact("Jane Smith", "555-5678", "456 Oak St"))

# Update a contact
new_contact = Contact("John Doe", "555-9999", "789 Pine St")
hash_table.update_contact("John Doe", new_contact)

# Verify the update
contact = hash_table.find_contact("John Doe")
if contact:
    print("Updated Contact:", contact)
else:
    print("Contact not found.")


def test_hash_table():
    # Create a hash table with open addressing
    hash_table = HashTable(size=10, method="open_addressing")

    # Add contacts to the hash table
    print("Adding contacts...")
    for i in range(8):  # Add fewer than the initial size to avoid immediate collisions
        contact = Contact(f"Contact{i}", f"555-01{i:02}", f"Address {i}")
        hash_table.add_contact(contact)

    # List all contacts after adding
    print("\nContacts after adding:")
    for contact in hash_table.list_contacts():
        print(contact)

    # Find a specific contact
    print("\nFinding Contact5:")
    contact = hash_table.find_contact(name="Contact5")
    print(contact)

    # Verify the update
    print("\nContact3 after update:")
    contact = hash_table.find_contact(name="Contact3")
    print(contact)

    # Delete a contact
    print("\nDeleting Contact2...")
    hash_table.delete_contact("Contact2")

    # Verify deletion
    print("\nContacts after deletion of Contact2:")
    for contact in hash_table.list_contacts():
        print(contact)

    # Add more contacts to test collisions
    print("\nAdding more contacts to test collisions...")
    for i in range(8, 15):
        contact = Contact(f"Contact{i}", f"555-02{i:02}", f"Address {i}")
        hash_table.add_contact(contact)

    # List all contacts after adding more
    print("\nContacts after adding more:")
    for contact in hash_table.list_contacts():
        print(contact)


if __name__ == "__main__":
    test_hash_table()
