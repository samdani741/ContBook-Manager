
def search_contacts(contact_book):
    found_search_result = False
    search_term = input("Searching Contact? \nEnter name, phone number, or email address for the search: ").lower()
    
    for contact in contact_book:
        if (search_term in contact["name"].lower() or 
            search_term in contact["phone"].lower() or 
            search_term in contact["email"].lower()):
            found_search_result = True
            print(f"\nFound: {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    
    if not found_search_result:
        print("No item found!")
