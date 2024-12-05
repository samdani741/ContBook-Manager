import create_contact_file
import view_all_contacts_file
import remove_contact
import search_contact

contact_book = []


print("Welcome!")

with open("contacts.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            contact = {
                "name": line_splitted[0],
                "phone": line_splitted[1],
                "email": line_splitted[2],
                "address": line_splitted[3],
            }
            contact_book.append(contact)



menu_text = """
Your options:
1. Create Contact
2. View All Contacts
3. Search Contacts
4. Remove Contact
0. Exit
"""

while True:
    print(menu_text)
    choice = input("Enter your choice: ")

    if choice == "1":
        contact_book = create_contact_file.create_contact(contact_book)
    elif choice == "2":
        view_all_contacts_file.view_all_contacts(contact_book)
    elif choice == "3":
        search_contact.search_contacts(contact_book)
    elif choice == "4":
        remove_contact.remove_contact(contact_book)
    elif choice == "0":
        print("Thank you for using Contact Book Management System")
        break
    else:
        print("Wrong Choice!\nTry Again!")
