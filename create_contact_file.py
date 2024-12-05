def create_contact(contact_book):
    # Input validation for name
    while True:
        name = input("Enter name: ")
        if not name.replace(" ", "").isalpha():
            print("ERROR: The contact's name must contain only letters and spaces. Please try again.")
            continue
        break

    # Input validation for phone
    while True:
        phone = input("Enter phone: ")
        if not phone.isdigit():
            print("ERROR: The phone number must be numeric. Please enter only digits.")
            continue
        if len(phone) < 10:
            print("ERROR: Phone number must be at least 10 digits long. Please try again.")
            continue
        break

    # Input validation for email
    while True:
        email = input("Enter email: ")
        if "@" not in email or "." not in email.split("@")[-1]:
            print("ERROR: Invalid email format. Please enter a valid email (e.g., example@domain.com).")
            continue
        break

    # Input validation for address
    while True:
        address = input("Enter address: ")
        if len(address.strip()) == 0:
            print("ERROR: Address cannot be empty. Please provide a valid address.")
            continue
        break

    # Check for duplicate phone number or email
    for contact in contact_book:
        if contact["phone"] == phone:
            print(f"ERROR: A contact with the phone number {phone} already exists.")
            return contact_book
        if contact["email"] == email:
            print(f"ERROR: A contact with the email address {email} already exists.")
            return contact_book

    # If no duplicates, add the new contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    }
    contact_book.append(contact)

    # Save the contact to a file
    with open("contacts.csv", "w") as file_pointer:
        for contact in contact_book:
            line = f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']}\n"
            file_pointer.write(line)

    print("Contact created successfully!")
    return contact_book
