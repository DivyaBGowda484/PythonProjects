import json
import os

# Contact Class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"

# ContactBook Class
class ContactBook:
    def __init__(self, file_path="contacts.json"):
        self.contacts = []
        self.file_path = file_path
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.contacts = [Contact(**c) for c in data]

    def save_contacts(self):
        with open(self.file_path, "w") as file:
            json.dump([c.to_dict() for c in self.contacts], file, indent=2)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        print(f"✅ Added: {contact.name}")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.")
            return
        print("\n📒 Contact List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact}")

    def search_contact(self, name):
        found = [c for c in self.contacts if c.name.lower() == name.lower()]
        if found:
            print(f"🔎 Found contact(s):")
            for c in found:
                print(c)
        else:
            print("❌ Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"🗑️ Deleted: {contact.name}")
                return
        print("❌ Contact not found.")

# CLI Menu
def main():
    book = ContactBook()

    while True:
        print("\n📱 Contact Book CLI")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact = Contact(name, phone, email)
            book.add_contact(contact)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            name = input("Enter Name to Search: ")
            book.search_contact(name)

        elif choice == '4':
            name = input("Enter Name to Delete: ")
            book.delete_contact(name)

        elif choice == '5':
            print("👋 Exiting Contact Book. Bye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

# Entry Point
if __name__ == "__main__":
    main()
