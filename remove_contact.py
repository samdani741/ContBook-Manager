def remove_contact(contact_book):
    # Search for the contact to remove
    search_term = input("Enter text to search to remove: ")
    matching_contacts = []
    
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact["name"].lower():
            matching_contacts.append((index, contact))
            print(f"{len(matching_contacts)}. {contact['name']} - {contact['phone']} - {contact['email']}")

    if not matching_contacts:
        print("No contacts found.")
        return contact_book

    # Ask user to select a contact to remove
    selected_index = input("Enter the number of the contact to remove: ")
    try:
        selected_index = int(selected_index)
        if 1 <= selected_index <= len(matching_contacts):
            actual_index = matching_contacts[selected_index - 1][0]
            contact_book.pop(actual_index)
            print("Contact removed successfully.")

            # Auto-save the updated contact book to the file
            with open("contacts.csv", "wt") as file_pointer:
                for contact in contact_book:
                    line = f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']}\n"
                    file_pointer.write(line)

        else:
            print("Invalid selection. No contact removed.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    return contact_book
