import unittest
from hash_table import HashTable, Contact


class TestHashTable(unittest.TestCase):
    def test_add_contact(self):
        ht = HashTable(size=5, method="separate_chaining")
        ht.add_contact(Contact("Alice", "555-1111", "123 Maple St"))
        self.assertIsNotNone(ht.find_contact("Alice"))

    def test_delete_contact(self):
        ht = HashTable(size=5, method="open_addressing")
        ht.add_contact(Contact("Bob", "555-2222", "456 Pine St"))
        ht.delete_contact("Bob")
        self.assertIsNone(ht.find_contact("Bob"))


if __name__ == "__main__":
    unittest.main()
