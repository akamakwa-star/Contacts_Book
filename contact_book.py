import json
import os

CONTACTS_FILE = "contacts.json"


# -----------------------------
# Load & Save Contacts
# -----------------------------
def load_contacts():
    """Load contacts from the JSON storage file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []


def sa_contacts(contacts):
    """Save contacts to the JSON storage file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# -----------------------------
# Add Contact
# -----------------------------
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("✔ Contact added successfully!\n")


# -----------------------------
# View All Contacts
# -----------------------------
def view_contacts():
    print("\n--- All Contacts ---")
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.\n")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    print()


# -----------------------------
# Search Contacts
# -----------------------------
def search_contacts():
    print("\n--- Search Contacts ---")
    keyword = input("Enter name, phone, or email: ").lower()

    contacts = load_contacts()
    results = [
        c for c in contacts
        if keyword in c["name"].lower()
        or keyword in c["phone"]
        or keyword in c["email"].lower()
    ]

    if results:
        print("\nSearch Results:")
        for c in results:
            print(f"- {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    else:
        print("No matching contacts found.")

    print()


# -----------------------------
# Update Contact
# -----------------------------
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Name of the contact to update: ").lower()

    contacts = load_contacts()

    for c in contacts:
        if c["name"].lower() == name:
            print("Leave an input empty to keep the existing value.\n")

            c["name"] = input(f"New name ({c['name']}): ") or c["name"]
            c["phone"] = input(f"New phone ({c['phone']}): ") or c["phone"]
            c["email"] = input(f"New email ({c['email']}): ") or c["email"]
            c["address"] = input(f"New address ({c['address']}): ") or c["address"]

            save_contacts(contacts)
            print("✔ Contact updated successfully!\n")
            return

    print("Contact not found.\n")


# -----------------------------
# Delete Contact
# -----------------------------
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Name of the contact to delete: ").lower()

    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(updated_contacts) == len(contacts):
        print("Contact not found.\n")
    else:
        save_contacts(updated_contacts)
        print("✔ Contact deleted successfully!\n")


# -----------------------------
# Menu System
# -----------------------------
def menu():
    while True:
        print("====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nSelect an option (1–6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    menu()
