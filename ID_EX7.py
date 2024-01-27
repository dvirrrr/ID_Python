"""
Itai Dvir
Dictionaries exercise program
"""
contacts = {}

def add_contact(name, phoneNumber):
    """
    get name, phoneNumber, function adds / updates a contact
    to contacts by the name and phone number.
    """
    phone_error = phoneNumber.isdigit()
    nametolist = name.split()
    name_error = [word.isalpha() for word in nametolist]
    if not phone_error:
        print(f"illegal phone number")
    if not all(name_error):
        print(f"illegal name")
    if phone_error and all(name_error):
        nametolist = [word.title() for word in nametolist]
        name = " ".join(nametolist)
        didExist = False
        for item in contacts:
            if item == name:
                contacts[item] = phoneNumber
                didExist = True
        if not didExist:
            contacts.update({name: phoneNumber})


def find_phone_number(name):
    """
    get name, find and return phone number by the name
    """
    rv = None
    nametolist = name.split()
    name_error = [word.isalpha() for word in nametolist]
    if not all(name_error):
        print(f"illegal name")
    else:
        nametolist = name.split()
        nametolist = [word.title() for word in nametolist]
        name = " ".join(nametolist)
        for item in contacts:
            if item == name:
                rv = contacts[item]
    return rv

def find_name(phone_number):
    """
    get phone_number, find and return name by phone_number
    """
    rv = None
    phone_error = phone_number.isdigit()
    if not phone_error:
        print(f"illegal phone number")
    else:
        for item in contacts:
            if contacts[item] == phone_number:
                rv = item
    return rv

def print_contacts_by_name():
    """
    print the contacts sorted by their name
    """
    sorted_contacts = dict(sorted(contacts.items()))
    for contact in sorted_contacts:
        print(f"name: {contact} -- phone: {contacts[contact]}")

def print_contacts_by_phone():
    """
    print the contacts sorted by their phone number
    """
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: item[1]))
    for contact, phone in sorted_contacts.items():
        print(f"name: {contact} -- phone: {phone}")

def merge_contacts(otherContacts):
    """
    get otherContacts, merge the other contacts
    with the main contacts variable.
    """
    for contact in otherContacts:
        contacts.update({contact : otherContacts[contact]})

def main():
    global contacts

    for _ in range(3):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    name_to_find = input("Enter a name to find its phone number: ")
    phone_number = find_phone_number(name_to_find)
    if phone_number:
        print(f"Phone number for {name_to_find}: {phone_number}")
    else:
        print("Name not in contacts")

    phone_to_find = input("Enter a phone number to find its name: ")
    contact_name = find_name(phone_to_find)
    if contact_name:
        print(f"Name for {phone_to_find}: {contact_name}")
    else:
        print("Phone number not in contacts")

    print("Contacts sorted by name:")
    print_contacts_by_name()

    friend_contacts = {'Itai': '0527287357', 'Omer': '6353464', 'Shlomi': '775777777'}
    merge_contacts(friend_contacts)
    print("Merged contacts sorted by name:")
    print_contacts_by_name()

if __name__ == "__main__":
    main()
