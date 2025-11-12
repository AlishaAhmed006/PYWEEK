def save_contact(name, number):
    with open("contacts.txt", "a") as file:
        file.write(name + " " + number + "\n")

def home():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts.append((name, number))
    save_contact(name, number)

def read_contacts():
    with open("contacts.txt", "r") as file:
        print("\nSaved Contacts:\n")
        print(file.read())

contacts = []
print("Contact System")
print("\n1. Add\n2. Read\n3. Exit")

opt = int(input("Enter your choice: "))

if opt == 1:
    home()
elif opt == 2:
    read_contacts()
