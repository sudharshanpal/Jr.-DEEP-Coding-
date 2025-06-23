# hosital queue challenge prototyping

# using dictonaries


queue_dict = {}

def add():
    name = input("What is your name: ")
    id = int(input("What is your patient id: "))
    queue_dict[id] = name
    print("Successfully Added.")

def remove():
    id = int(input("What ID do you want to remove: "))

    if id in queue_dict:
        queue_dict.pop(id)
        print("Successfully Removed.")
    else:
        print("ID does not exist in queue")

def checkDup():
    check = input("Enter ID or Name to check if it exists: ")

    if check.isdigit():
        if int(check) in queue_dict:
            print("Duplicate ID found.")
            return

    for x in queue_dict.values():
        if x == check:
            print("Duplicate Name found.")
            return
    print("No duplicates found.")

while True:

    #print out the menu
    print("MENU:")
    print("1. Add patient")
    print("2. Remove patient")
    print("3. Show Queue")
    print("4. Check Duplicate")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    if choice == 3:
        print(queue_dict)
    if choice == 1:
        add()
    if choice == 2:
        remove()
    if choice == 4:
        checkDup()