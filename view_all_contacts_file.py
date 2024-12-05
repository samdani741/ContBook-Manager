def view_all_contacts(contact_book):
    # Define the headers
    headers = ["Name", "Phone", "Email", "Address"]
    
    # Calculate column widths based on the longest value in each column
    col_widths = [
        max(len(contact.get("name", "")) for contact in contact_book),
        max(len(contact.get("phone", "")) for contact in contact_book),
        max(len(contact.get("email", "")) for contact in contact_book),
        max(len(contact.get("address", "")) for contact in contact_book),
    ]
    
    # Adjust for headers if they're longer than any contact data
    col_widths = [max(len(header), width) for header, width in zip(headers, col_widths)]
    
    # Print the header row
    header_row = " | ".join(header.ljust(width) for header, width in zip(headers, col_widths))
    print(header_row)
    print("-" * len(header_row))  # Separator line
    
    # Print each contact
    for contact in contact_book:
        row = " | ".join(
            contact.get(field, "").ljust(width)
            for field, width in zip(["name", "phone", "email", "address"], col_widths)
        )
        print(row)
