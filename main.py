# Contact Book

Contact = []

while True:
    print("\n ===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add Contact 
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        Contact.append(contact)
        print("Contact added successfully!")

    # View Contacts
    elif choice == '2':
        if not Contact:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for i, contact in enumerate(Contact, start =1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    # Search Contact
    elif choice == '3':
        search_name = input("Enter contact name to search: ")
        found_contacts = [contact for contact in Contact if search_name.lower() in contact['name'].lower()]
        if found_contacts:
            print("\nFound Contacts:")
            for i, contact in enumerate(found_contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts found.")

    # Delete Contact
    elif choice == '4':
        if not Contact:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for i, contact in enumerate(Contact, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            delete_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= delete_index < len(Contact):
                del Contact[delete_index]
                print("Contact deleted successfully!")
            else:
                print("Invalid contact number.")

    # Exit 
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")